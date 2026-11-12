"""CPU build and Make dependency graph regressions; CUDA is never invoked."""
from pathlib import Path
import math
import re
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class A5BuildTests(unittest.TestCase):
    def test_serial_build_and_bounded_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            build = Path(directory) / "build"
            build.mkdir()
            (build / "Execution_logs").mkdir()
            objects = Path(directory) / "objects"
            # Run a copied Makefile from an isolated tree: no tracked binaries change.
            for source in (ROOT / "a5").iterdir():
                if source.is_file() and source.suffix in [".c", ".h", ".cu"]:
                    (build / source.name).symlink_to(source)
            (build / "Helper_functions").symlink_to(ROOT / "a5/Helper_functions", target_is_directory=True)
            command = ["make", "-f", str(ROOT / "a5/Makefile"), "kmeans_seq", "OBJECT_DIR=" + str(objects)]
            run = subprocess.run(command, cwd=build, capture_output=True, text=True, timeout=30)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            result = subprocess.run([str(build / "kmeans_seq"), "-c", "2", "-s", "0.001", "-n", "2", "-l", "3"], cwd=build, capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            centers = re.findall(r"clusters\[\d+\] = ([^\n]+)", result.stdout)
            self.assertEqual(len(centers), 2)
            self.assertTrue(all(math.isfinite(float(value)) for row in centers for value in row.split()))

    def test_supported_default_excludes_unfinished_reduction(self):
        run = subprocess.run(["make", "-B", "-n", "all", "NVCC=/usr/bin/false"], cwd=ROOT / "a5", capture_output=True, text=True, timeout=5)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertNotIn("cuda_kmeans_all_gpu_delta_reduction.cu", run.stdout)
        self.assertIn("cuda_kmeans_all_gpu.cu", run.stdout)


if __name__ == "__main__":
    unittest.main()

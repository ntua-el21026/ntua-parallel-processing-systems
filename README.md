# Parallel_Processing_Systems

Coursework and lab assignments from the Parallel Processing Systems course (NTUA ECE). The repository spans shared-memory, GPU, and distributed-memory programming in C/CUDA with OpenMP and MPI, plus benchmarking scripts and reports.

## Repository structure
- `a1/`: OpenMP Game of Life (introductory parallelization and timing).
- `a2/`: OpenMP K-means and Floyd-Warshall (shared-memory optimization).
- `a3/`: K-means with multiple lock implementations to study synchronization costs.
- `a4/`: Concurrent sorted linked list with coarse/fine/optimistic/lazy/lock-free variants.
- `a5/`: CUDA K-means with progressively optimized GPU kernels.
- `a6/`: MPI K-means and 2D heat transfer (Jacobi and related solvers).
- `docs/`: assignment PDFs, lecture slides, and reports.
- `shell_scripts/`: helper scripts for running on the lab infrastructure.

Each assignment directory contains its own `README.md` with the specific task description, key files, and outputs. The detailed methodology and results are captured in `docs/reports/`.

## Team, provenance and release status

The final report credits Michail-Athanasios Peppas and Andreas Saounatsos. The project combines team implementations with NTUA CSLab starter code; retain all file-level notices, including Vasileios Karakasis/CSLab attribution in `a5/Helper_functions/alloc.c`. Per-person ownership has not been reconstructed from the imported tree. Handouts, lecture slides and external source assets need their own redistribution review; the root MIT notice covers original contributions only within the authors' rights.

This is a conditional public systems showcase. A deleted lab-access file remains reachable in historical commits. Its password must be treated as exposed until the owner confirms revocation/rotation, including any reuse. It was not tested, printed, restored, or rewritten out of history during preparation. A current-file cleanup does not resolve that historical exposure.

## Local setup and supported execution

Use Linux, GCC/G++ and make for the CPU exercises; OpenMP requires the compiler's OpenMP runtime. Assignment 5 additionally needs a compatible NVIDIA CUDA toolkit/GPU, and Assignment 6 needs an MPI toolchain. Inspect each Makefile and scheduler script before use: lab account/module/path settings are site-specific and not a portable environment specification. Do not run queue submission scripts as part of setup.

The CPU-only regression suite creates temporary build/output directories and never invokes CUDA or a scheduler:

```bash
python3 -m unittest discover -s tests -v
```

It builds and executes a tiny serial K-means case and checks the default build dependency graph. Assignment 5 now uses the actual `Helper_functions` path on case-sensitive filesystems and creates the object directory for a fresh build. `make -C a5 kmeans_seq` is the CPU target; `make -C a5 all NVCC=/path/to/nvcc` builds the implemented CPU/CUDA set. The unfinished delta-reduction kernel is available only through explicit `experimental`; it is not a supported correctness/performance implementation.

Before timing a GPU/MPI/OpenMP variant, compare with its serial/reference result under the declared validation mode and tolerance. Record compiler flags, exact source/configuration, random input provenance, process/thread counts, hardware/topology and repeated measurements. Historical queue logs/reports remain evidence of their original runs; preparation did not rerun GPU/MPI or certify general performance claims.

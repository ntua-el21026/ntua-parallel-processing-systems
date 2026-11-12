# a5 - GPU K-means with CUDA

This assignment moves K-means clustering to NVIDIA GPUs using CUDA. The goal is to compare increasingly optimized GPU kernels and quantify the impact of memory access patterns and host-device transfers.

## Assignment focus
- Naive GPU offload (membership on GPU, centroid update on CPU).
- Data layout optimization (transpose/column-major) for memory coalescing.
- Shared-memory centroids to reduce global memory traffic.
- Full GPU version with atomics for centroid updates.

The report in `../docs/reports/individual/a5/` walks through each kernel variant and the performance analysis.

## Contents
- `cuda_kmeans_naive.cu`, `cuda_kmeans_transpose.cu`, `cuda_kmeans_shared.cu`, `cuda_kmeans_all_gpu.cu`: kernel variants.
- `main_gpu.cu`, `main_sec.c`, `seq_kmeans.c`: drivers and reference code.
- `Makefile`, `make_on_queue.sh`, `run_on_queue.sh`: build and queue scripts.
- `validation_results.txt`, `validate_on_queue.sh`: correctness checks.
- `diagrams/`, `Execution_logs/`: plots and run logs.

## Build status

`make kmeans_seq` builds the serial target with G++ and no CUDA dependency. A
fresh build creates `ObjectDir`; the helper path is `Helper_functions` with a
capital H. The serial executable writes under `Execution_logs`, so keep that
directory writable and keep new logs separate from historical results.

`make all NVCC=/path/to/nvcc` includes the four implemented CUDA variants listed
above. CUDA architecture flags remain historical (`sm_60`) and require review
for the actual toolkit/GPU; no GPU compatibility was validated in preparation.
`cuda_kmeans_all_gpu_delta_reduction.cu` has unfinished thread-index/reduction
scaffolding and is excluded from `all`. `make experimental` is explicitly opt-in
for investigation, without an algorithmic correctness claim.

Run the repository's bounded CPU/build regressions with
`python3 -m unittest discover -s tests -v` from the root. These checks do not run
the GPU kernels. Preserve CSLab/helper-code notices and validate against serial
before measuring any newly supported GPU variant.

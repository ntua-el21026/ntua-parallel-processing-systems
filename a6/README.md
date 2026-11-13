# a6 - Distributed Memory (MPI)

This assignment targets distributed-memory parallelism using MPI. It includes two workloads: K-means clustering and 2D heat transfer.

## Assignment focus
- MPI K-means: distribute points, compute local contributions, and combine centroids with collective reductions.
- 2D heat transfer: grid decomposition with halo exchanges and convergence checks (Jacobi, with Gauss-Seidel and Red-Black variants available in the codebase).
- Measure total time vs computation time and study speedup across process counts.

The [assignment report](../docs/reports/individual/a6/) summarizes the MPI design, timing methodology, and scalability results.

## Contents
- `kmeans/`: MPI K-means implementation, benchmarks, and run scripts.
- `heat_transfer/`: MPI heat transfer kernels and benchmarks (Jacobi, Gauss-Seidel SOR, Red-Black SOR).
- `diagrams/`: plotting scripts and generated figures.
- `docs/`: assignment PDFs.

See the [repository guide](../README.md) for toolchain separation, PBS assumptions, attribution, and measurement limits.

## Build and scheduler notes

From the repository root, use `make -C a6/kmeans` for `kmeans_mpi` and `make -C a6/heat_transfer/mpi` for `jacobi_mpi`, `gauss_mpi`, and `redblack_mpi`. The latter Makefile's target names are `jacobi`, `gauss`, and `redblack`; executable names include the `_mpi` suffix. `make -C a6/heat_transfer/serial` builds the serial references.

PBS scripts assume the original course modules, host resources, and launch options. The serial heat-transfer `make_on_queue.sh` and `run_on_queue.sh` contain literal `cd <FIX PATH>` placeholders; both fail `bash -n` until those template paths are adapted. The scripts are preserved unchanged. No MPI program or queue job was executed during this documentation update.

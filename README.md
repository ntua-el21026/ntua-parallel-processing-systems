# NTUA Parallel Processing Systems

Six NTUA ECE assignments in C/CUDA covering shared-memory parallelism, synchronization, GPU kernels, and distributed-memory programming. Source, scheduler scripts, benchmark logs, diagrams, and original reports are retained together.

## Assignment guide

| Assignment | Implemented workloads | Execution requirements |
| --- | --- | --- |
| [a1: Game of Life](a1/README.md) | OpenMP grid updates and timing | GCC with OpenMP |
| [a2: K-means and Floyd–Warshall](a2/README.md) | Shared-memory clustering, reduction, and shortest-path variants | GCC with OpenMP |
| [a3: Synchronization costs](a3/README.md) | K-means with critical sections, pthread mutex/spin, TAS/TTAS, array, and CLH locks | GCC, OpenMP, and pthreads |
| [a4: Concurrent sorted list](a4/README.md) | Serial, coarse/fine-grained, optimistic, lazy, and nonblocking variants | GCC and pthreads; Linux affinity helpers |
| [a5: CUDA K-means](a5/README.md) | Serial reference, naive, transpose, shared-memory, and full-GPU variants | G++ for serial; compatible NVIDIA GPU/toolkit for CUDA |
| [a6: MPI](a6/README.md) | Distributed K-means and heat-transfer solvers | MPI compiler/runtime; GCC for serial references |

[Course material and reports](docs/README.md) explain methodology and historical results. Each component guide links its implementation and evidence. The `benchmarks/`, `Execution_logs/`, and report directories retain original measurements; do not replace them during a new run.

## Build requirements and entry points

```bash
git clone https://github.com/ntua-el21026/ntua-parallel-processing-systems.git
cd ntua-parallel-processing-systems
```

There is no repository-wide build. From the repository root, select the relevant component:

| Component | Build command | Principal targets |
| --- | --- | --- |
| Game of Life | `make -C a1` | `life_par` |
| OpenMP K-means | `make -C a2/kmeans` | `seq_kmeans`, `omp_naive_kmeans`, `omp_reduction_kmeans` |
| Floyd–Warshall | `make -C a2/FW` | `fw`, `fw_sr_p`, `fw_tiled` |
| K-means locks | `make -C a3` | `kmeans_omp_*` variants listed in its Makefile |
| Concurrent list | `make -C a4/conc_ll` | `x.serial`, `x.cgl`, `x.fgl`, `x.opt`, `x.lazy`, `x.nb` |
| Serial CUDA-assignment reference | `make -C a5 kmeans_seq` | `kmeans_seq`, using `Helper_functions/` and `ObjectDir/` |
| MPI K-means | `make -C a6/kmeans` | `kmeans_mpi` |
| MPI heat transfer | `make -C a6/heat_transfer/mpi` | `jacobi_mpi`, `gauss_mpi`, `redblack_mpi` |

CPU shared-memory components need the appropriate OpenMP/pthread support; MPI components need `mpicc` and a compatible launcher. Assignment 5's `make all NVCC=/path/to/nvcc` includes four implemented CUDA variants, with historical `sm_60` flags requiring review against the actual toolkit/GPU. The unfinished delta-reduction source is deliberately available only via `make experimental`; it has no supported correctness or performance claim.

## Scheduler and infrastructure assumptions

The `make_on_queue.sh`/`run_on_queue.sh` scripts target the course's PBS environment, with `#PBS` resource requests, `module load` commands, lab-account paths, and sometimes fixed output filenames. Assignment 6's K-means runner requests eight nodes/eight processes per node, loads `openmpi/1.8.3`, and uses a site-specific `--mca btl tcp,self` option. These are historical execution assumptions, not a portable cluster configuration. The serial heat-transfer `make_on_queue.sh` and `run_on_queue.sh` still contain literal `cd <FIX PATH>` placeholders and fail Bash syntax checking until adapted in a local copy.

Review paths, modules, resource limits, process/thread counts, and output destinations before submitting any job. Do not submit benchmark matrices as part of installation. [SSH/SSHFS helpers](shell_scripts/README.md) also contain original WSL/lab-account paths and require local adaptation; they are not needed to inspect or build the source.

## Validation and measurement

The existing CPU-only regression suite uses temporary build/output directories:

```bash
python3 -m unittest discover -s tests -v
```

It contains two tests: a tiny serial K-means build/run and inspection of the default build graph. It does not execute CUDA, MPI, queue jobs, or concurrent-list correctness tests.

Before timing a new OpenMP/CUDA/MPI variant, compare its result against the serial/reference implementation using the declared validation mode and tolerance. Record compiler flags, source/configuration/input hashes, random initialization, process/thread counts, hardware/topology, and repeated measurements. Queue logs and reports support only their original workload/hardware settings.

## Team and starter code

The final report credits **Michail-Athanasios Peppas and Andreas Saounatsos**. Implementations build on NTUA CSLab starter code; retain all file-level notices, including Vasileios Karakasis/CSLab attribution in `a5/Helper_functions/alloc.c`.

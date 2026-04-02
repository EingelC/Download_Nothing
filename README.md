# Trixie Update Simulator
A Python-based terminal utility designed to simulate the Debian package management process for the trixie distribution. This script provides a high-fidelity visual representation of network synchronization, package retrieval, and filesystem decompression.

## Technical Overview
The simulation utilizes the `tqdm` library for progress visualization and `numpy` for localized data distribution. It replicates the behavior of advanced package managers by splitting tasks into two distinct phases:

1. Retrieval (Get): Simulates binary download with configurable file sizes and network throughput fluctuations.

2. Unpacking: Simulates the extraction of .deb archives with a stabilized processing rate to mimic disk I/O operations.

## Environment Configuration
The following parameters are hardcoded to maintain consistency with the target environment:

- **CODENAME:** trixie
- **ARCH:** amd64
- **DATABASE:** A structured dictionary containing Kernel, Library, System, and Shared Object package metadata.

## Installation
The script requires Python and the following dependencies:
- tqdm
- Numpy

```Bash
pip install tqdm numpy
```
## Execution
To initialize the update simulation, execute the core script:

```Bash
python main.py
```
To terminate the process, use the standard interrupt signal (SIGINT) via `Ctrl+C`.

## Customization
### Data Volume
The file size ranges can be modified within the `simular_proceso` function. Adjust the total variable to redefine the workload for each phase:

- ***Network Phase:*** np.random.randint(min, max) in Megabytes.

- ***Processing Phase:*** np.random.randint(min, max) in total iterations.

## Operational Stability
The "jitter" logic ensures the progress bar moves without erratic jumps. The fluctuation margin is currently set to 8% of the base step to provide a consistent visual flow.

## Disclaimer
This software is a simulation tool. It does not modify system binaries, install actual software, or require administrative privileges.

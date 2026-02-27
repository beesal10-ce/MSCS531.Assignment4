# MSCS531.Assignment4
# gem5 Instruction-Level Parallelism (ILP) Study

This repository contains the practical exploration of ILP techniques using the gem5 simulator. 

## Contents
- **Report**: Full analysis of Baseline, Branch Prediction, Superscalar, and SMT configurations.
- **Scripts**: `ilp_study.py` used for parameter-driven simulations.
- **Results**: IPC and Tick data extracted from gem5 statistics.

## Key Findings
Throughput (IPC) was heavily limited by instruction cache latency (the "Memory Wall"). Increasing pipeline width (Superscalar) did not improve performance without accompanying memory hierarchy optimizations.

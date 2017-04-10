# cube-config

This repository contains the scripts as well as the configurations used for individual Earth System Data Cube (ESDC) productions. 

# Cube generation

## Pre-requisites

* cablab-core
* cube directory (where the generated data will be located)

## Generation

1. `git clone https://github.com/CAB-LAB/cube-config.git`
2. `cd cube-config/<cube version directory>`
3. Run the following:
   * **Windows**: `cube-gen-all.bat <source directory> <cube directory>`
   * **Linux**: `./cube-gen-all.sh <source directory> <cube directory>`

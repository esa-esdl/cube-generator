# cube-config

This repository contains the scripts as well as the configurations used for individual Earth System Data Cube (ESDC) productions. 

# Cube generation

## Pre-requisites

* Miniconda
  * Install [Miniconda](https://conda.io/miniconda.html)
  * `cd cablab-core`
  * `conda env create --file=environment.yml`
  * `source activate esdc` (Linux) or `activate esdc` (Windows)
* cablab-core
  * `git clone https://github.com/CAB-LAB/cablab-core.git`
  * `cd cablab-core`
  * `python setup.py install`
* cube directory (where the generated data will be located)
  * `mkdir <cube directory name>` 

## Generation

1. `git clone https://github.com/CAB-LAB/cube-config.git`
2. `cd cube-config/<cube version directory>`
3. Run the following:
   * **Windows**: `cube-gen-all.bat <source directory> <cube directory>`
   * **Linux**: `./cube-gen-all.sh <source directory> <cube directory>`

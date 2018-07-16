# cube-generator

This repository contains the scripts as well as the configurations used for individual Earth System Data Cube (ESDC) productions. 

## Cube generation

### Pre-requisites

* esdl-core
  * `git clone https://github.com/esa-esdl/esdl-core.git`
  * `cd esdl-core`
  * `python setup.py install`
* Miniconda
  * Install [Miniconda](https://conda.io/miniconda.html)
  * `cd esdl-core`
  * `conda env create --file=environment.yml`
  * `source activate esdl` (Linux) or `activate esdl` (Windows)

### Generation

1. `git clone https://github.com/esa-esdl/cube-generator.git`
2. `cd cube-generator/scripts`
3. Run the following:
   * **Windows**: `cube-gen.bat <cube-high-res.config|cube-low-res.config|cube-super-low-res.config> <source directory> <cube directory>`
   * **Linux**: `./cube-gen.sh <cube-high-res.config|cube-low-res.config|cube-super-low-res.config> <source directory> <cube directory>`
   **NOTE**: Use the following naming convention for the cube directory name: https://github.com/esa-esdl/cube-generator/wiki/Cube-file-structure-and-naming-convention

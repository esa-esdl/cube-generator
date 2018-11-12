# Earth System Data Cube Version 1.0.2_2 (ESDCv1.0.2_2)

This repository contains the scripts, configurations as well as providers used for individual Earth System Data Cube (ESDC) productions. The repository also contains md5 sums of the released data. 

## Cube generation

### Pre-requisites

* Miniconda
  * Install [Miniconda](https://conda.io/miniconda.html)
  * `cd esdl-core`
  * `conda env create --file=environment.yml`
  * `source activate esdl` (Linux) or `activate esdl` (Windows)
* esdl-core
  * activate esdl miniconda env (see previous steps)
  * `git clone https://github.com/esa-esdl/esdl-core.git`
  * `cd esdl-core`
  * `python setup.py install`

### Generation

1. `git clone https://github.com/esa-esdl/cube-generator.git`
2. `cd cube-generator/scripts`
3. Run the following:
   * **Windows**: `cube-gen.bat <cube-high-res.config|cube-low-res.config|cube-super-low-res.config> <source directory> <cube directory>`
   * **Linux**: `./cube-gen.sh <cube-high-res.config|cube-low-res.config|cube-super-low-res.config> <source directory> <cube directory>`

**NOTE**: Use the following naming convention for the cube directory name: https://github.com/esa-esdl/cube-generator/wiki/Cube-file-structure-and-naming-convention

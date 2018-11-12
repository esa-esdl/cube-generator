# Earth System Data Cube Version 1.0.2_2 (ESDCv1.0.2_2)

This repository contains the scripts, configurations as well as providers used for individual Earth System Data Cube (ESDC) productions. The repository also contains md5 sums of the released data. 

## Cube generation

### Install Pre-requisites for cube generation

* Miniconda
  * Install [Miniconda](https://conda.io/miniconda.html)
* Install cate
  * `git clone https://github.com/esa-esdl/cube-generator.git`
  * `cd [cube-generator]/cate`
  * `conda env create --file=environment.yml`
  * `source activate cate` (Linux) or `activate esdl` (Windows)
  * `python setup.py  install`
* Install esdl-core
  * `cd [cube-generator]/esdl-core`
  * `python setup.py install`
  * Run `cuge-gen` to test whether the software is correctly installed

### Generation

The esdl core library contains data providers already. However, for this version we developed new
providers for new and updated variables. They are stored in teh sub directory `cube/providers`. In order
to activate them, you have to run `python setup.py` from the cube-generator root directory. 

### Adding and updating Variables for v1.0.2_2

1. `cd [cube-generator]/scripts`
3. Run the following:
   * **Windows**: `cube-gen.bat`
   * **Linux**: `./cube-gen.sh`

**NOTE**: Use the following naming convention for the cube directory name: https://github.com/esa-esdl/cube-generator/wiki/Cube-file-structure-and-naming-convention

# Earth System Data Cube Version 1.0.2_2 (ESDCv1.0.2_2)

This repository contains the scripts, configurations as well as providers used for individual Earth System Data Cube (ESDC) production of version 1.0.2_2. 
The repository also contains md5 sums of the released data.

The version 1.0.2_2 comtains compared to version 1.0.2_1 of the following
additional variables:

- 1

The following variables were updated:

- 1

Version 1.0.2_2 uses the zarr format. Old formatted cubes can be found in
the attic of teh ESDC platform. 

## Cube generation

### Installing Pre-requisites for the Cube Generation

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

### Providers

The esdl core library contains data providers already. However, for this version we developed new
providers for new and updated variables. They are stored in the sub-directory `cube/providers`. In order
to activate them, you have to run `python setup.py` from the cube-generator root directory. 

### Adding and updating Variables for v1.0.2_2

1. `cd [cube-generator]/scripts`
2. rsync down cube
3. check md5sums
4. Run the following:
   * **Windows**: `cube-gen.bat`
   * **Linux**: `./cube-gen.sh`
5. Copy new variables to cube
6. Generate md5sums of new variable
7. rsync cube up
8. commit new md5sums to repo

The cube version 1.0.2_2 uses the zarr data format. Zarr serialises chunked
data and, thus, is comprised of a large number of small files for each variable.
For the generation we have, therefore, used the following bash commands for each 
variable:

```
for v in $(ls -d [cube])
do
    find -f file [cube]/$v > [cube]/$v.md 
done
```

Checking the md5sum will need

```
for v in $(ls -d [cube])
do
    find -f file [cube]/$v > [cube]/$v.md
done
```

## Naming convention

The following naming convention for the cube directories has been used: https://github.com/esa-esdl/cube-generator/wiki/Cube-file-structure-and-naming-convention



# The ESDC data cube v 1.0.2_2


## Usage



__Open a Cube (config: 8d, 0.25deg)__

```
import xarray as xr
ds = xr.open_zarr('/home/jovyan/work/datacube/ESDCv1.0.2_2/esdc-8d-0.25deg-1x720x1440-1.0.2_2.zarr')
ds
```


__Open a variable (e.g. par)__

```

ds.par

```

__Plot a time step__

```

v = ds.par.sel(time='2003-01-05')
v.plot()

```

__Plot a regional subset__:

```

v = ds.par.loc[dict(lat=slice(40, -20), lon=slice(-20, 20), time='2003-01-05')]
v.plot()
```


__Plot a time step close to your choice__

```

v = ds.par.sel(time='2003-01-08', method='nearest')
v.plot()

```


__Plot a time series of a cell close to a spatial location__


```
v = ds.par.sel(dict(lat=51, lon=10), method='nearest')
v.plot()

```


# cube-generator

This repository contains the scripts as well as the configurations used for individual Earth System Data Cube (ESDC) productions. 

## Roadmap

* Release of version 2.0.0 (Xmas 2018)
  - Meta data fixed and completed
  - Cube documented
  - Examples given
  - Cube in Object store
  - Implementation of a proper versioning scheme
* Visualisation of uncertainty (information entropy)
* Adding a dynamic data loader from daily updated data (e.g. TEMIS)

# Earth System Data Cube Version 1.0.2_2 (ESDCv1.0.2_2)

This repository contains the scripts, configurations as well as providers used for individual Earth System Data Cube (ESDC) production of version 1.0.2_2. 
The repository also contains md5 sums of the released data.

The version 1.0.2_2 contains compared to version 1.0.2_1 of the following
additional variables:

- air_temperature_2m
- analysed_sst
- AOD1600_mean
- AOD550_mean
- AOD670_mean
- AOD870_mean
- cee
- cer
- cfc
- chlor_a
- cot
- cph
- cth
- ctp
- ctt
- fat_c
- fat_p
- flt_c
- flt_p
- free_fat_c
- free_flt_c
- free_lrt_c
- free_msr_flt
- free_msr_lrt
- iwp
- lrt_c
- lrt_p
- lwp
- mask
- msr_flt
- msr_lrt
- nobs
- precipitation_era5
- psurf
- sea_ice_fraction
- totcol_assim
- totcol_free
- totcol_msr
- white_sky_albedo_avhrr
- xch4
-xco2


The following variables were updated:

- ozone 
- All aerosol variables


Version 1.0.2_2 uses the zarr format. Old formatted cubes can be found in
the attic of teh ESDC platform. 

## Meta Info

- [1/12th degree cube](metainfo/ESDL_metadata_cube_high.csv)


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
4. `./cube-gen.sh`
5. Copy new variables to cube
6. Generate md5sums of new variable
7. rsync cube up
8. commit new md5sums to repo

The cube version 1.0.2_2 uses the zarr data format. Zarr serialises chunked
data and, thus, is comprised of a large number of small files for each variable.

The following script will generate a total md5sums for each directory.

```
bash scripts/checksum.sh -c [cube]
```

This script will check the integrity of the md5sums across a cube:

```
bash check_data_integrity.sh -c [cube]
```

## Naming convention

The following naming convention for the cube directories has been used: https://github.com/esa-esdl/cube-generator/wiki/Cube-file-structure-and-naming-convention


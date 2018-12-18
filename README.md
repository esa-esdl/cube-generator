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

## Meta Info Cube 1/12th Degree

| Attribute                | Value                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| title                    | Earth System Data Cube                                                                                         |
| summary                  | This data set contains a data cube of Earth System variables created by the ESA project Earth System Data Lab. |
| keywords                 | Earth Science - Geophysical Variables                                                                          |
| id                       | v1.0.2_2                                                                                                       |
| naming_authority         | Earth System Data Lab team                                                                                     |
| history                  | processed with esdl cube v0.1  (https://github.com/esa-esdl/esdl-core/)                                        |
| comment                  | none                                                                                                           |
| date_created             | 2018-12-01                                                                                                     |
| creator_name             | Brockmann Consult GmbH                                                                                         |
| creator_url              | www.earthsystemdatalab.net                                                                                     |
| creator_email            | info@earthsystemdatalab.net                                                                                    |
| institution              | Brockmann Consult GmbH                                                                                         |
| project                  | ESA Earth System Data Lab                                                                                      |
| processing_level         | Level 4                                                                                                        |
| acknowledgment           | The ESDL team acknowledges all data providers!                                                                 |
| geospatial_lat_min       | -89.95761                                                                                                      |
| geospatial_lat_max       | 89.958336                                                                                                      |
| geospatial_lon_min       | -179.95833                                                                                                     |
| geospatial_lon_max       | 179.9569                                                                                                       |
| geospatial_resolution    | 1/12 deg                                                                                                       |
| chunking                 | 1x2160x4320                                                                                                    |
| time_coverage_start      | 1980-01-05                                                                                                     |
| time_coverage_end        | 2016-12-31                                                                                                     |
| time_coverage_duration   | 13509d                                                                                                         |
| time_coverage_resolution | 8d                                                                                                             |
| standard_name_vocabulary | CF-1.7                                                                                                         |
| license                  | Please refer to individual variables                                                                           |
| contributor_name         | Max Planck Institute for Biogeochemistry                                                                       |
| contributor_role         | ESDL Science Lead                                                                                              |
| publisher_name           | Brockmann Consult GmbH & Max Planck Institute for Biogechemistry                                               |
| publisher_url            | www.brockmann-consult.de                                                                                       |
| publisher_email          | info@earthsystemdatalab.net                                                                                    |
| date_modified            | 2018-12-17                                                                                                     |
| date_issued              | 2018-12-19                                                                                                     |
| Metadata_conventions     | Unidata Dataset Discovery v1.0                                                                                 |


## Meta Info Cube 1/4th Degree

| Attribute                | Value                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| title                    | Earth System Data Cube                                                                                         |
| summary                  | This data set contains a data cube of Earth System variables created by the ESA project Earth System Data Lab. |
| keywords                 | Earth Science - Geophysical Variables                                                                          |
| id                       | v1.0.2_2                                                                                                       |
| naming_authority         | Earth System Data Lab team                                                                                     |
| history                  | processed with esdl cube v0.1  (https://github.com/esa-esdl/esdl-core/)                                        |
| comment                  | none                                                                                                           |
| date_created             | 2018-12-01                                                                                                     |
| creator_name             | Brockmann Consult GmbH                                                                                         |
| creator_url              | www.earthsystemdatalab.net                                                                                     |
| creator_email            | info@earthsystemdatalab.net                                                                                    |
| institution              | Brockmann Consult GmbH                                                                                         |
| project                  | ESA Earth System Data Lab                                                                                      |
| processing_level         | Level 4                                                                                                        |
| acknowledgment           | The ESDL team acknowledges all data providers!                                                                 |
| geospatial_lat_min       | -89.75                                                                                                         |
| geospatial_lat_max       | 89.75                                                                                                          |
| geospatial_lon_min       | -179.75                                                                                                        |
| geospatial_lon_max       | 179.75                                                                                                         |
| geospatial_resolution    | 1/4 deg                                                                                                        |
| chunking                 | 1x720x1440                                                                                                     |
| time_coverage_start      | 1980-01-05                                                                                                     |
| time_coverage_end        | 2016-12-31                                                                                                     |
| time_coverage_duration   | 13509d                                                                                                         |
| time_coverage_resolution | 8d                                                                                                             |
| standard_name_vocabulary | CF-1.7                                                                                                         |
| license                  | Please refer to individual variables                                                                           |
| contributor_name         | Max Planck Institute for Biogeochemistry                                                                       |
| contributor_role         | ESDL Science Lead                                                                                              |
| publisher_name           | Brockmann Consult GmbH & Max Planck Institute for Biogechemistry                                               |
| publisher_url            | www.brockmann-consult.de                                                                                       |
| publisher_email          | info@earthsystemdatalab.net                                                                                    |
| date_modified            | 2018-12-17                                                                                                     |
| date_issued              | 2018-12-19                                                                                                     |
| Metadata_conventions     | Unidata Dataset Discovery v1.0                                                                                 |


## Metainfo Variables

Refer to (CSV document)[metainfo/ESDL_metadata_variables.csv]

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


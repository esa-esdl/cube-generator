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

| project_name                                                        | long_name                                                 | url                                                               | esa_cci_path                                                                      | orig_version | vname                             | coverage_start | coverage_end |  |
| ------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------ | --------------------------------- | -------------- | ------------ |  |
| BESS                                                                | Diffuse Photosynthetically Active Radiation               | http://environment.snu.ac.kr/bess_rad/                            |                                                                                   | 15.10.2017   | pardiff                           | 2000-03-01     | 2016-12-30   |  |
| BESS                                                                | Downwelling shortwave radiation                           | http://environment.snu.ac.kr/bess_rad/                            |                                                                                   | 15.10.2017   | Rg                                | 2000-03-01     | 2010-12-31   |  |
| BESS                                                                | Photosynthetically Active Radiation                       | http://environment.snu.ac.kr/bess_rad/                            |                                                                                   | 15.10.2017   | par                               | 2000-03-01     | 2016-12-30   |  |
| ERA5                                                                | 2 Metre Air Temperature                                   | https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation |                                                                                   | ERA5         | air_temperature_2m                | 2000-01-05     | 2016-12-30   |  |
| ERA5                                                                | ERA5 Precipitation                                        | https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation |                                                                                   | ERA5         | precipitation_era5                | 2000-01-05     | 2016-12-30   |  |
| ERA5                                                                | Maximum 2 Metre Air Temperature                           | https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation |                                                                                   | ERA5         | max_air_temperature_2m            | 2000-01-05     | 2016-12-30   |  |
| ERA5                                                                | Minimum 2 Metre Air Temperature                           | https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation |                                                                                   | ERA5         | min_air_temperature_2m            | 2000-01-05     | 2016-12-30   |  |
| ESA - Near-real time total ozone column (OMI)                       | Residual MSR-FLT (Stratospheric Part Partial)             | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | free_msr_flt                      | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Residual MSR-FLT (Stratospheric Part Partial)             | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | msr_flt                           | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Residual MSR-LRT (Stratospheric Part Partial)             | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | free_msr_lrt                      | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Residual MSR-LRT (Stratospheric Part Partial)             | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | msr_lrt                           | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Surface Air Pressure                                      | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | psurf                             | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Total Ozone Column (Assimilated TM5 data)                 | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | totcol_assim                      | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Total Ozone Column (Assimilated TM5 data)                 | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | totcol_free                       | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Total Ozone Column (MSR data)                             | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | totcol_msr                        | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropopause Air Pressure (Lapse Rate)                      | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | lrt_p                             | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropopause Air Pressure for the Fixed Altitude Tropopause | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | fat_p                             | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropopause Air Pressure for the Fixed Layer Tropopause    | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | flt_p                             | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropospheric Ozone Column                                 | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | flt_c                             | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropospheric Ozone Column ( Lapse Rate)                   | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | free_lrt_c                        | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropospheric Ozone Column (Fixed Altitude)                | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | fat_c                             | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropospheric Ozone Column (Fixed Altitude)                | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | free_fat_c                        | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropospheric Ozone Column (Fixed Layers)                  | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | free_flt_c                        | 2008-01-05     | 2011-12-31   |  |
| ESA - Near-real time total ozone column (OMI)                       | Tropospheric Ozone Column (Lapse Rate)                    | http://www.temis.nl/protocols/tropo.html                          |                                                                                   | v.1.2.3.1    | lrt_c                             | 2008-01-05     | 2011-12-31   |  |
| ESA Aerosol CCI                                                     | Aerosol optical thickness at 1600 nm                      | http://www.esa-aerosol-cci.org/                                   | /neodc/esacci/aerosol/data/AATSR_SU/L3/v4.21/DAILY/                               | v4.21        | AOD1600_mean                      | 2002-07-24     | 2012-04-10   |  |
| ESA Aerosol CCI                                                     | Aerosol optical thickness at 550 nm                       | http://www.esa-aerosol-cci.org/                                   | /neodc/esacci/aerosol/data/AATSR_SU/L3/v4.21/DAILY/                               | v4.21        | AOD550_mean                       | 2002-07-24     | 2012-04-10   |  |
| ESA Aerosol CCI                                                     | Aerosol optical thickness at 670 nm                       | http://www.esa-aerosol-cci.org/                                   | /neodc/esacci/aerosol/data/AATSR_SU/L3/v4.21/DAILY/                               | v4.21        | AOD670_mean                       | 2002-07-24     | 2012-04-10   |  |
| ESA Aerosol CCI                                                     | Aerosol optical thickness at 870 nm                       | http://www.esa-aerosol-cci.org/                                   | /neodc/esacci/aerosol/data/AATSR_SU/L3/v4.21/DAILY/                               | v4.21        | AOD870_mean                       | 2002-07-24     | 2012-04-10   |  |
| ESA CCI Ocean Colour Product                                        | Chlorophyll-a Concentration in Seawater                   | http://esa-oceancolour-cci.org                                    | /neodc/esacci/ocean_colour/data/v3.1-release/geographic/netcdf/chlor_a/daily/v3.1 | v3.1         | chlor_a                           | 1997-09-02     | 2016-12-30   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Effective Emissivity at 10.8 um                     | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | cee                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Effective Radius                                    | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | cer                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud fraction                                            | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | cfc                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Ice Water Path                                      | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | iwp                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Liquid Water Path                                   | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | lwp                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Optical Thickness                                   | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | cot                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Top Height                                          | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | cth                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Top Pressure                                        | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | ctp                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Cloud Top Temperature                                     | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | ctt                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Fraction of Liquid Water Clouds                           | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | cph                               | 2000-01-29     | 2014-12-31   |  |
| ESA Cloud Climate Change Initiative (Cloud_cci)                     | Surface Temperature                                       | http://www.dwd.de                                                 | /neodc/esacci/cloud/data/phase-2/L3C/MODIS-TERRA/v2.0/                            | v2.0         | stemp                             | 2000-01-29     | 2014-12-31   |  |
| ESA Greenhouse Gases Climate Change Initiative (GHG_cci)            | Column Average Dry-air Mole Fraction Carbon Dioxide       | http://www.esa-ghg-cci.org/                                       | /neodc/esacci/ghg/data/obs4mips/crdp_3/CO2/v100/                                  | v100         | xco2                              | 2003-01-13     | 2014-12-15   |  |
| ESA Greenhouse Gases Climate Change Initiative (GHG_cci)            | Column Average Dry-air Mole Fraction Methane              | http://www.esa-ghg-cci.org/                                       | /neodc/esacci/ghg/data/obs4mips/crdp_3/CO2/v100/                                  | v100         | xch4                              | 2003-01-13     | 2014-12-15   |  |
| ESA Land Cover Climate Change Initiative (Land_Cover_cci)           | Terrestrial or Water Pixel Classification                 | http://www.esa-landcover-cci.org                                  | /neodc/esacci/land_cover/data/water_bodies/v4.0/                                  | v4.0         | water_mask                        | 1980-01-05     | 1980-01-05   |  |
| ESA Sea Surface Temperature Climate Change Initiative (ESA SST CCI) | Analysed Sea Surface Temperature                          | http://www.esa-sst-cci.org                                        | /neodc/esacci/sst/data/lt/Analysis/L4/v01.1/                                      | v01.1        | analysed_sst                      | 1991-09-02     | 2010-12-31   |  |
| ESA Sea Surface Temperature Climate Change Initiative (ESA SST CCI) | Sea Ice Area Fraction                                     | http://www.esa-sst-cci.org                                        | /neodc/esacci/sst/data/lt/Analysis/L4/v01.1/                                      | v01.1        | sea_ice_fraction                  | 1991-09-02     | 2010-12-31   |  |
| ESA Sea Surface Temperature Climate Change Initiative (ESA SST CCI) | Sea/Land/Lake/Ice Field Composite Mask                    | http://www.esa-sst-cci.org                                        | /neodc/esacci/sst/data/lt/Analysis/L4/v01.1/                                      | v01.1        | mask                              | 1991-09-02     | 2010-12-31   |  |
| FLUXCOM                                                             | Gross Primary Productivity                                | http://www.fluxcom.org/                                           |                                                                                   | v1           | gross_primary_productivity        | 2001-01-05     | 2015-12-31   |  |
| FLUXCOM                                                             | Latent Energy                                             | http://www.fluxcom.org/                                           |                                                                                   | v1           | latent_energy                     | 2001-01-05     | 2015-12-31   |  |
| FLUXCOM                                                             | Net Ecosystem Exchange                                    | http://www.fluxcom.org/                                           |                                                                                   | v1           | net_ecosystem_exchange            | 2001-01-05     | 2015-12-31   |  |
| FLUXCOM                                                             | Net Radiation                                             | http://www.fluxcom.org/                                           |                                                                                   | v1           | net_radiation                     | 2001-01-05     | 2015-12-31   |  |
| FLUXCOM                                                             | Sensible Heat                                             | http://www.fluxcom.org/                                           |                                                                                   | v1           | sensible_heat                     | 2001-01-05     | 2015-12-31   |  |
| FLUXCOM                                                             | Terrestrial Ecosystem Respiration                         | http://www.fluxcom.org/                                           |                                                                                   | v1           | terrestrial_ecosystem_respiration | 2001-01-05     | 2012-12-30   |  |
| GFED4                                                               | Carbon Dioxide Emissions Due to Natural Fires             | http://www.globalfiredata.org/                                    |                                                                                   | gfed4        | c_emissions                       | 2001-01-05     | 2010-12-31   |  |
| GFED4                                                               | Monthly Burnt Area                                        | http://www.globalfiredata.org/                                    |                                                                                   | gfed4        | burnt_area                        | 1995-01-05     | 2014-03-02   |  |
| GLEAM                                                               | Bare Soil Evaporation                                     | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | bare_soil_evaporation             | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Evaporation                                               | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | evaporation                       | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Evaporative Stress Factor                                 | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | evaporative_stress                | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Interception Loss                                         | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | interception_loss                 | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Open-Water Evaporation                                    | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | open_water_evaporation            | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Potential Evaporation                                     | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | potential_evaporation             | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Root-Zone Soil Moisture                                   | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | root_moisture                     | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Snow Sublimation                                          | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | snow_sublimation                  | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Surface Soil Moisture                                     | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | surface_moisture                  | 2003-01-05     | 2016-12-30   |  |
| GLEAM                                                               | Transpiration                                             | http://www.gleam.eu                                               |                                                                                   | Version 3.2  | transpiration                     | 2003-01-05     | 2016-12-30   |  |
| GlobAlbedo                                                          | Black Sky Albedo for Visible Wavebands                    | http://www.globalbedo.org/                                        |                                                                                   |              | black_sky_albedo                  | 1998-01-05     | 2012-01-05   |  |
| GlobAlbedo                                                          | White Sky Albedo for Visible Wavebands                    | http://www.globalbedo.org/                                        |                                                                                   |              | white_sky_albedo                  | 1998-01-05     | 2012-01-05   |  |
| GlobSnow                                                            | Daily Snow Water Equivalent                               | http://www.globsnow.info/                                         |                                                                                   | v2.0         | snow_water_equivalent             | 1980-01-05     | 2012-12-30   |  |
| GlobSnow                                                            | Surface Fraction Covered by Snow                          | http://www.globsnow.info/                                         |                                                                                   | v2.0         | fractional_snow_cover             | 2003-01-05     | 2013-01-05   |  |
| GlobTemperature                                                     | Land Surface Temperature                                  | http://data.globtemperature.info/                                 |                                                                                   |              | land_surface_temperature          | 2002-05-21     | 2011-12-31   |  |
| GlobVapour                                                          | Total Column Water Vapour                                 | http://www.globvapour.info/                                       |                                                                                   |              | water_vapour                      | 1996-01-05     | 2008-12-30   |  |
| GPCP                                                                | Precipitation                                             | http://precip.gsfc.nasa.gov/                                      |                                                                                   |              | precipitation                     | 1980-01-05     | 2015-01-05   |  |
| Ozone CCI                                                           | Mean Total Ozone Column in dobson units                   | http://www.esa-ozone-cci.org/                                     | /neodc/esacci/ozone/data/total_columns/l3/merged/v0100/                           | v0100        | ozone                             | 1996-03-09     | 2011-06-30   |  |
| QA4ECV                                                              | Effective Leaf Area Index                                 | http://www.qa4ecv.eu/                                             |                                                                                   |              | leaf_area_index                   | 1982-01-05     | 2016-12-30   |  |
| QA4ECV                                                              | Fraction of Absorbed PAR                                  | http://www.qa4ecv.eu/                                             |                                                                                   |              | fapar_tip                         | 1982-01-05     | 2016-12-30   |  |
| QA4ECV - European Union Framework Program 7                         | Bi-Hemisphere Reflectance Albedo - VIS band               | http://www.qa4ecv.eu/                                             |                                                                                   |              | white_sky_albedo_avhrr            | 1982-01-05     | 2016-12-30   |  |
| QA4ECV - European Union Framework Program 7                         | Directional Hemisphere Reflectance albedo - VIS band      | http://www.qa4ecv.eu/                                             |                                                                                   |              | black_sky_albedo_avhrr            | 1982-01-05     | 2016-12-30   |  |
| regionmask - SREX Regions                                           | Mask for SREX Regions                                     | https://regionmask.readthedocs.io/                                |                                                                                   |              | srex_mask                         | 1980-01-05     | 1980-01-05   |  |
| SoilMoisture CCI                                                    | Soil Moisture                                             | http://www.esa-soilmoisture-cci.org                               | /neodc/esacci/soil_moisture/data/daily_files/COMBINED/v04.2/                      | v04.2        | soil_moisture                     | 1980-01-05     | 2014-01-29   |  |


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


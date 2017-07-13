#!/usr/bin/env bash

source_dir=$1
cube_path=$2

cube_config_low_res="cube-low-res.config"

STARTTIME=$(date)

cube-gen "$cube_path\low-res" "burnt_area:dir=$source_dir\BurntArea" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "aerosols:dir=$source_dir\CCI-Aerosols\AATSR_SU_v4.1\L3_DAILY" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "air_temperature:dir=$source_dir\T2m-ECMWF\low" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "albedo:dir=$source_dir\globalbedo_CF_compliant\\05deg\\8daily" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "c_emissions:dir=$source_dir\Fire_C_Emissions" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "root_moisture:dir=$source_dir\GLEAM\v3a_BETA:var=SMroot" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "evaporation:dir=$source_dir\GLEAM\v3a_BETA:var=E" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "evaporative_stress:dir=$source_dir\GLEAM\v3a_BETA:var=S" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "potential_evaporation:dir=$source_dir\GLEAM\v3a_BETA:var=Ep" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "interception_loss:dir=$source_dir\GLEAM\v3a_BETA:var=Ei" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "surface_moisture:dir=$source_dir\GLEAM\v3a_BETA:var=SMsurf" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "bare_soil_evaporation:dir=$source_dir\GLEAM\v3a_BETA:var=Eb" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "snow_sublimation:dir=$source_dir\GLEAM\v3a_BETA:var=Es" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "transpiration:dir=$source_dir\GLEAM\v3a_BETA:var=Et" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "open_water_evaporation:dir=$source_dir\GLEAM\v3a_BETA:var=Ew" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "globvapour:dir=$source_dir\globvapour\GOME_SCIA_GOME2\monthly" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "land_surface_temperature:dir=$source_dir\globtemperature\ftp2.globtemperature.info\AATSR\L3" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "ozone:dir=$source_dir\Ozone-CCI\Total_Columns\L3\MERGED" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "precip:dir=$source_dir\CPC_precip" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "snow_area_extent:dir=$source_dir\SnowAreaExtent:resampling_order=space_first" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "snow_water_equivalent:dir=$source_dir\SWE" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "soil_moisture:dir=$source_dir\ECV_sm" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "gross_primary_production:dir=$source_dir\MPI_BGC\GPP:var=GPPall" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "sensible_heat:dir=$source_dir\MPI_BGC\H:var=H" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "latent_energy:dir=$source_dir\MPI_BGC\LE:var=LE" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "net_ecosystem_exchange:dir=$source_dir\MPI_BGC\NEE:var=NEE" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "terrestrial_ecosystem_respiration:dir=$source_dir\MPI_BGC\TER:var=TERall" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "country_mask:dir=$source_dir\CountryCodes-ISO3166" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "water_mask:dir=$source_dir\WaterBodies4.0" -c $cube_config_low_res
cube-gen "$cube_path\low-res" "srex_mask:dir=$source_dir\SREX_mask" -c $cube_config_low_res

ENDTIME=$(date)

echo STARTTIME: $STARTTIME
echo ENDTIME: $ENDTIME

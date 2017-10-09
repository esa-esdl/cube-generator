#!/usr/bin/env bash

source_dir=$1
cube_path=$2

cube_config_low_res="cube-low-res.config"

STARTTIME=$(date)

cube-gen "$cube_path" "burnt_area:dir=$source_dir/BurntArea" -c $cube_config_low_res
cube-gen "$cube_path" "aerosols:dir=$source_dir/CCI-Aerosols/AATSR_SU_v4.1/L3_DAILY"
cube-gen "$cube_path" "air_temperature:dir=$source_dir/T2m-ECMWF/low"
cube-gen "$cube_path" "albedo:dir=$source_dir/globalbedo_CF_compliant/05deg/8daily"
cube-gen "$cube_path" "c_emissions:dir=$source_dir/Fire_C_Emissions"
cube-gen "$cube_path" "root_moisture:dir=$source_dir/GLEAM/v3a_BETA:var=SMroot"
cube-gen "$cube_path" "evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=E"
cube-gen "$cube_path" "evaporative_stress:dir=$source_dir/GLEAM/v3a_BETA:var=S"
cube-gen "$cube_path" "potential_evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=Ep"
cube-gen "$cube_path" "interception_loss:dir=$source_dir/GLEAM/v3a_BETA:var=Ei"
cube-gen "$cube_path" "surface_moisture:dir=$source_dir/GLEAM/v3a_BETA:var=SMsurf"
cube-gen "$cube_path" "bare_soil_evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=Eb"
cube-gen "$cube_path" "snow_sublimation:dir=$source_dir/GLEAM/v3a_BETA:var=Es"
cube-gen "$cube_path" "transpiration:dir=$source_dir/GLEAM/v3a_BETA:var=Et"
cube-gen "$cube_path" "open_water_evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=Ew"
cube-gen "$cube_path" "globvapour:dir=$source_dir/globvapour/GOME_SCIA_GOME2/monthly"
cube-gen "$cube_path" "land_surface_temperature:dir=$source_dir/globtemperature/ftp2.globtemperature.info/AATSR/L3"
cube-gen "$cube_path" "ozone:dir=$source_dir/Ozone-CCI/Total_Columns/L3/MERGED"
cube-gen "$cube_path" "precip:dir=$source_dir/CPC_precip"
cube-gen "$cube_path" "snow_area_extent:dir=$source_dir/SnowAreaExtent:resampling_order=space_first"
cube-gen "$cube_path" "snow_water_equivalent:dir=$source_dir/SWE"
cube-gen "$cube_path" "soil_moisture:dir=$source_dir/ECV_sm"
cube-gen "$cube_path" "gross_primary_production:dir=$source_dir/MPI_BGC/GPP:var=GPPall"
cube-gen "$cube_path" "sensible_heat:dir=$source_dir/MPI_BGC/H:var=H"
cube-gen "$cube_path" "latent_energy:dir=$source_dir/MPI_BGC/LE:var=LE"
cube-gen "$cube_path" "net_ecosystem_exchange:dir=$source_dir/MPI_BGC/NEE:var=NEE"
cube-gen "$cube_path" "terrestrial_ecosystem_respiration:dir=$source_dir/MPI_BGC/TER:var=TERall"
cube-gen "$cube_path" "country_mask:dir=$source_dir/CountryCodes-ISO3166"
cube-gen "$cube_path" "water_mask:dir=$source_dir/WaterBodies4.0"
cube-gen "$cube_path" "srex_mask:dir=$source_dir/SREX_mask"

ENDTIME=$(date)

echo STARTTIME: $STARTTIME
echo ENDTIME: $ENDTIME

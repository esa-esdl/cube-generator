#!/usr/bin/env bash

source_dir=$1
cube_path=$2

cube_config_high_res="cube-high-res.config"

STARTTIME=$(date)

cube-gen "$cube_path/high-res" "burnt_area:dir=$source_dir/BurntArea" -c $cube_config_high_res
cube-gen "$cube_path/high-res" "aerosols:dir=$source_dir/CCI-Aerosols/AATSR_SU_v4.1/L3_DAILY"/
cube-gen "$cube_path/high-res" "air_temperature:dir=$source_dir/T2m-ECMWF/low"/
cube-gen "$cube_path/high-res" "albedo:dir=$source_dir/globalbedo_CF_compliant/05deg/8daily"/
cube-gen "$cube_path/high-res" "c_emissions:dir=$source_dir/Fire_C_Emissions"/
cube-gen "$cube_path/high-res" "root_moisture:dir=$source_dir/GLEAM/v3a_BETA:var=SMroot"/
cube-gen "$cube_path/high-res" "evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=E"/
cube-gen "$cube_path/high-res" "evaporative_stress:dir=$source_dir/GLEAM/v3a_BETA:var=S"/
cube-gen "$cube_path/high-res" "potential_evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=Ep"/
cube-gen "$cube_path/high-res" "interception_loss:dir=$source_dir/GLEAM/v3a_BETA:var=Ei"/
cube-gen "$cube_path/high-res" "surface_moisture:dir=$source_dir/GLEAM/v3a_BETA:var=SMsurf"/
cube-gen "$cube_path/high-res" "bare_soil_evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=Eb"/
cube-gen "$cube_path/high-res" "snow_sublimation:dir=$source_dir/GLEAM/v3a_BETA:var=Es"/
cube-gen "$cube_path/high-res" "transpiration:dir=$source_dir/GLEAM/v3a_BETA:var=Et"/
cube-gen "$cube_path/high-res" "open_water_evaporation:dir=$source_dir/GLEAM/v3a_BETA:var=Ew"/
cube-gen "$cube_path/high-res" "globvapour:dir=$source_dir/globvapour/GOME_SCIA_GOME2/monthly"/
cube-gen "$cube_path/high-res" "land_surface_temperature:dir=$source_dir/globtemperature/ftp2.globtemperature.info/AATSR/L3"/
cube-gen "$cube_path/high-res" "ozone:dir=$source_dir/Ozone-CCI/Total_Columns/L3/MERGED"/
cube-gen "$cube_path/high-res" "precip:dir=$source_dir/CPC_precip"/
cube-gen "$cube_path/high-res" "snow_area_extent:dir=$source_dir/SnowAreaExtent:resampling_order=space_first"/
cube-gen "$cube_path/high-res" "snow_water_equivalent:dir=$source_dir/SWE"/
cube-gen "$cube_path/high-res" "soil_moisture:dir=$source_dir/ECV_sm"/
cube-gen "$cube_path/high-res" "gross_primary_production:dir=$source_dir/MPI_BGC/GPP:var=GPPall"/
cube-gen "$cube_path/high-res" "sensible_heat:dir=$source_dir/MPI_BGC/H:var=H"/
cube-gen "$cube_path/high-res" "latent_energy:dir=$source_dir/MPI_BGC/LE:var=LE"/
cube-gen "$cube_path/high-res" "net_ecosystem_exchange:dir=$source_dir/MPI_BGC/NEE:var=NEE"/
cube-gen "$cube_path/high-res" "terrestrial_ecosystem_respiration:dir=$source_dir/MPI_BGC/TER:var=TERall"/
cube-gen "$cube_path/high-res" "country_mask:dir=$source_dir/CountryCodes-ISO3166"/
cube-gen "$cube_path/high-res" "water_mask:dir=$source_dir/WaterBodies4.0"/
cube-gen "$cube_path/high-res" "srex_mask:dir=$source_dir/SREX_mask"/

ENDTIME=$(date)

echo STARTTIME: $STARTTIME
echo ENDTIME: $ENDTIME

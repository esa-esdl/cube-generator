#!/usr/bin/env bash

cube_path=$1
cube_provider=$2
source_dir=$3
cube_config=$4

START_TIME=$(date)

bsub -W 12:00 -M 64000 -e ozone_h.err -o ozone_h.out -J ozone_h cube-gen esdc/ozone/esdc-8d-0.25deg-1x720x1440-1.0.2 "ozone:dir=ozone" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e ozone_l.err -o ozone_l.out -J ozone_l cube-gen esdc/ozone/esdc-8d-0.083deg-1x2160x4320-1.0.2 "ozone:dir=ozone" -c cube-high-res.config
bsub -W 12:00 -M 64000 -e aerosol_l.err -o aerosol_l.out -J aerosol_l cube-gen esdc/aerosol/esdc-8d-0.25deg-1x720x1440-1.0.2 "aerosols:dir=aerosol" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e aerosol_h.err -o aerosol_h.out -J aerosol_h cube-gen esdc/aerosol/esdc-8d-0.083deg-1x2160x4320-1.0.2 "aerosols:dir=aerosol" -c cube-high-res.config
bsub -W 12:00 -M 64000 -e ch4_l.err -o ch4_l.out -J ch4_l cube-gen esdc/ch4/esdc-8d-0.25deg-1x720x1440-1.0.2 "ch4:dir=CH4" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e ch4_h.err -o ch4_h.out -J ch4_h cube-gen esdc/ch4/esdc-8d-0.083deg-1x2160x4320-1.0.2 "ch4:dir=CH4" -c cube-high-res.config
bsub -W 12:00 -M 64000 -e co2_l.err -o co2_l.out -J co2_l cube-gen esdc/co2/esdc-8d-0.25deg-1x720x1440-1.0.2 "co2:dir=CO2" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e co2_h.err -o co2_h.out -J co2_h cube-gen esdc/co2/esdc-8d-0.083deg-1x2160x4320-1.0.2 "co2:dir=CO2" -c cube-high-res.config
bsub -W 12:00 -M 64000 -e ozone_temis_l.err -o ozone_temis_l.out -J ozone_temis_l cube-gen esdc/ozone_temis/esdc-8d-0.25deg-1x720x1440-1.0.2 "ozone_temis:dir=ozone_temis" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e ozone_temis_h.err -o ozone_temis_h.out -J ozone_temis_h cube-gen esdc/ozone_temis/esdc-8d-0.083deg-1x2160x4320-1.0.2 "ozone_temis:dir=ozone_temis" -c cube-high-res.config


bsub -W 12:00 -M 64000 -e cloud_l.err -o cloud_l.out -J cloud_l cube-gen esdc/cloud/esdc-8d-0.25deg-1x720x1440-1.0.2 "cloud:dir=cloud" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e cloud_h.err -o cloud_h.out -J cloud_h cube-gen esdc/cloud/esdc-8d-0.083deg-1x2160x4320-1.0.2 "cloud:dir=cloud" -c cube-high-res.config

bsub -W 12:00 -M 64000 -e soil_l.err -o soil_l.out -J soil_l cube-gen esdc/soil_moisture/esdc-8d-0.25deg-1x720x1440-1.0.2 "soil_moisture_esacci:dir=soil_moisture_tt" -c cube-low-res.config
bsub -W 12:00 -M 64000 -e soil_h.err -o soil_h.out -J soil_h cube-gen esdc/soil_moisture/esdc-8d-0.083deg-1x2160x4320-1.0.2 "soil_moisture_esacci:dir=soil_moisture_tt" -c cube-high-res.config

bsub -W 23:00 -M 64000 -e sst_l.err -o sst_l.out -J sst_l cube-gen esdc/sst/esdc-8d-0.25deg-1x720x1440-1.0.2 "sst:dir=sst" -c cube-low-res.config
bsub -W 23:00 -M 64000 -e sst_h.err -o sst_h.out -J sst_h cube-gen esdc/sst/esdc-8d-0.083deg-1x2160x4320-1.0.2 "sst:dir=sst" -c cube-high-res.config

bsub -W 23:00 -M 64000 -e oc_l.err -o oc_l.out -J oc_l cube-gen esdc/oc/esdc-8d-0.25deg-1x720x1440-1.0.2 "oc:dir=OC-daily" -c cube-low-res.config
bsub -W 23:00 -M 64000 -e oc_h.err -o oc_h.out -J oc_h cube-gen esdc/oc/esdc-8d-0.083deg-1x2160x4320-1.0.2 "oc:dir=OC-daily" -c cube-high-res.config


END_TIME=$(date)

echo "Source:  ${source_dir}"
echo "Config: ${cube_config}"
echo "Provider: ${cube_provider}"
echo "Output: ${cube_path}"
echo STARTTIME: ${START_TIME}
echo ENDTIME: ${END_TIME}

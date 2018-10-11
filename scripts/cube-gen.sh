#!/usr/bin/env bash

cube_path=$1
cube_provider=$2
source_dir=$3
cube_config=$4

START_TIME=$(date)

cube-gen "$cube_path" "$cube_provider:dir=$source_dir" -c ${cube_config}

END_TIME=$(date)

echo "Source:  ${source_dir}"
echo "Config: ${cube_config}"
echo "Provider: ${cube_provider}"
echo "Output: ${cube_path}"
echo STARTTIME: ${START_TIME}
echo ENDTIME: ${END_TIME}

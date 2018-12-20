#!/bin/bash

usage="$(basename "$0") [-h] [-c cube] -- Generating md5sums for each variable's directory.

where:
    -h  show this help text
    -c  data cube"

cube=''
while getopts ':hc:' option; do
  case "$option" in
    h) echo "$usage"
       exit
       ;;
    c) cube=$OPTARG
       ;;
    :) printf "missing argument for -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "illegal option: -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))



for d in $(ls -d ${cube}/* | grep -v '.md5')
do
    echo Processing ${d}
    find $d -type f -exec md5sum {} \; | sort -k 2 | md5sum > ${d}.md5
done

#!/usr/bin/env bash

cat cube_list.txt | while read line
do
	echo echo ${line} | awk '{print "cube-gen.sh "$1" "$2" "$3" "$4}'
done 

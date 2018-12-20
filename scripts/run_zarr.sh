
rm -rf out_vars/esdc-8d-0.083deg-1x2160x4320-1.0.2_2/$1
bsub -e log/$1.err -o log/$1.out -M 512000 -W 12:00 -q high-mem -n 8  python convert_zarr.py esdc-8d-0.083deg-1x2160x4320-1.0.2_2 $1
#bsub -e $1.err -o $1.out -M 32000 -W 12:00 -q par-multi -n 128  python convert_zarr.py esdc-8d-0.083deg-1x2160x4320-1.0.2_2 $1

import xarray as xr
import esdl
import sys

EXTRA_COORDS_VAR_NAMES = ['time_bnds', 'lat_bnds', 'lon_bnds']

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

in_cube = sys.argv[1]
var = sys.argv[2]
zarr_cube = sys.argv[3]

var_loc = in_cube + '/data/' + var

print('opening template' + 'tpls/' + zarr_cube + '.zarr')
tpl = xr.open_zarr('tpls/' + zarr_cube + '.zarr')
print('opening variable')
a = xr.open_mfdataset(var_loc + '/*.nc')
a = a.chunk({'time': 1})

for var_name in EXTRA_COORDS_VAR_NAMES:
    if var_name in a.data_vars:
        a.set_coords(var_name, inplace=True)

a = a.chunk({'time': 46, 'lat': 270, 'lon': 270})

print('merging')
res = xr.merge([tpl, a])
res = res.chunk({'time': 46})

print('zarring')
res.to_zarr('out/' + zarr_cube + '/' + var + '.zarr')
res.close()




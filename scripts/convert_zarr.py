import xarray as xr
import esdl
import sys

EXTRA_COORDS_VAR_NAMES = ['time_bnds', 'lat_bnds', 'lon_bnds']

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

cube = sys.argv[1]
var = sys.argv[2]

var_loc = 'netcdf_cubes/' + cube + '/data/' + var


print('opening template' + 'tpls/' + cube + '.zarr')
tpl = xr.open_zarr('tpls/' + cube + '.zarr')
print('opening variable')
a = xr.open_mfdataset(var_loc + '/*.nc')

for var_name in EXTRA_COORDS_VAR_NAMES:
    if var_name in a.data_vars:
        a.set_coords(var_name, inplace=True)

print('merging')
res = xr.merge([tpl, a])
res = res.chunk({'time': 1})

print('zarring')
res.to_zarr('out_vars/' + cube + '/' + var + '.zarr')
res.close()




import xarray as xr
import esdl

ds = xr.open_mfdataset('esdc-8d-0.083deg-46x270x270-1.0.2_1/data/*/*.nc')

EXTRA_COORDS_VAR_NAMES = ['time_bnds', 'lat_bnds', 'lon_bnds']

for var_name in EXTRA_COORDS_VAR_NAMES:
    if var_name in ds.data_vars:
        ds.set_coords(var_name, inplace=True)

ds = ds.chunk({'time': 46, })
ds.to_zarr('tpls/esdc-8d-0.083deg-46x270x270-1.0.2_1.zarr')
ds.close()


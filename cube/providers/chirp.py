# uncompyle6 version 3.2.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 | packaged by conda-forge | (default, Oct 12 2018, 14:08:43) 
# [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
# Embedded file name: /home/users/hdzierz/cube-generator/cube/providers/sst.py
# Compiled at: 2018-11-09 05:37:39
# Size of source mod 2**32: 2979 bytes
import os
from datetime import datetime
from dateutil.parser import parse
import netCDF4, numpy, xarray as xr
from esdl.cate.cube_gen import CateCubeSourceProvider
import pandas as pd

class CHIRPProvider(CateCubeSourceProvider):

    def __init__(self, cube_config, name='chirp', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    _attrs = {'title':'CHIRP  Version 1.0', 
     'data_type':numpy.float32, 
     'fill_value':numpy.nan, 
     'url':'http://chg.geog.ucsb.edu/data/chirps/index.html', 
     'project':'Climate Change Initiative - European Space Agency', 
     'source_version':'1.0', 
     'source_dir':'website download'}

    @property
    def variable_descriptors(self):
        ds = xr.open_dataset(self.dir_path + '/chirp.1981.days_p05.nc')
        meta = dict()
        meta.update(self._attrs)
        meta.update(ds.attrs)
        coords = ('longitude', 'latitude', 'time')
        res = dict()
        for vs in ds.variables:
            if vs not in coords:
                if 'standard_name' not in ds[vs].attrs:
                    standard_name = vs
                else:
                    standard_name = ds[vs].standard_name
                meta_var = {'source_name':vs, 
                 'long_name':ds[vs].long_name, 
                 'standard_name':standard_name, 
                 'geostatial_lat_min:':ds[vs].geostatial_lat_min, 
                 'geostatial_lat_max:':ds[vs].geostatial_lat_max, 
                 'geostatial_lon_min:':ds[vs].geostatial_lon_min,
                 'geostatial_lon_max:':ds[vs].geostatial_lon_max,
                 'source':''}
                if 'units' in ds[vs].attrs:
                    meta_var['units'] = ds[vs].units
                meta_var.update(meta)
                res[vs] = meta_var

        ds.close()
        return res

    def compute_source_time_ranges(self):
        source_time_ranges = list()
        for root, sub_dirs, files in os.walk(self.dir_path, followlinks=True):
            for file_name in files:
                if '.nc' in file_name:
                    f = os.path.join(root, file_name)
                    ds = xr.open_dataset(f)
                    t1 = pd.to_datetime(ds.time.min().values)
                    t2 = pd.to_datetime(ds.time.max().values)
                    ds.close()
                    source_time_ranges.append((t1, t2, f, 0))

        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.flipud(source_image)

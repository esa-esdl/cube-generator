# uncompyle6 version 3.2.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 | packaged by conda-forge | (default, Oct 12 2018, 14:08:43) 
# [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
# Embedded file name: /home/users/hdzierz/cube-generator/cube/providers/soil_moisture_esacci.py
# Compiled at: 2018-11-08 12:49:04
# Size of source mod 2**32: 2853 bytes
import os
from datetime import datetime
from dateutil.parser import parse
import netCDF4, numpy, xarray as xr
from esdl.cate.cube_gen import CateCubeSourceProvider

class SoilMoistureESACCIProvider(CateCubeSourceProvider):

    def __init__(self, cube_config, name='soil_moisture_esacci', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    _attrs = {'title':'ESA Cloud CCI Retrieval Products L3 Output File', 
     'data_type':numpy.float32, 
     'fill_value':numpy.nan, 
     'url':'http://www.dwd.de', 
     'project':'Climate Change Initiative - European Space Agency'}

    @property
    def variable_descriptors(self):
        ds = xr.open_dataset(self.dir_path + '/2000/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-20000101000000-fv04.2.nc')
        meta = dict()
        meta.update(self._attrs)
        meta.update(ds.attrs)
        coords = ('lon', 'lat', 'time')
        res = dict()
        for vs in ds.variables:
            if vs not in coords:
                if '_' not in vs:
                    if vs not in ('time', 'lat', 'lon', 't0'):
                        if 'standard_name' not in ds[vs].attrs:
                            standard_name = vs
                        else:
                            standard_name = ds[vs].standard_name
                        meta_var = {'source_name':vs, 
                         'long_name':ds[vs].long_name, 
                         'standard_name':standard_name}
                        if 'units' in ds[vs].attrs:
                            meta_var['units'] = ds[vs].units
                        if 'valid_range' in ds[vs].attrs:
                            meta_var['valid_range'] = ds[vs].valid_range
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
                    t = file_name.split('-')
                    t = datetime.strptime(t[5], '%Y%m%d%H%M%S')
                    source_time_ranges.append((t, t, f, 0))

        print(source_time_ranges)
        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.flipud(source_image)
        

# uncompyle6 version 3.2.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.6 | packaged by conda-forge | (default, Oct 12 2018, 14:08:43) 
# [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
# Embedded file name: /home/users/hdzierz/cube-generator/cube/providers/cloud.py
# Compiled at: 2018-11-07 13:32:15
# Size of source mod 2**32: 2924 bytes
import os
from datetime import datetime
from dateutil.parser import parse
import netCDF4, numpy, xarray as xr
from esdl.cate.cube_gen import CateCubeSourceProvider

class CloudProvider(CateCubeSourceProvider):

    def __init__(self, cube_config, name='cloud', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    _attrs = {'title':'ESA Cloud CCI Retrieval Products L3 Output File', 
     'data_type':numpy.float32, 
     'fill_value':numpy.nan, 
     'url':'http://www.dwd.de', 
     'project':'Climate Change Initiative - European Space Agency'}

    @property
    def variable_descriptors(self):
        ds = xr.open_dataset(self.dir_path + '/2000/200002-ESACCI-L3C_CLOUD-CLD_PRODUCTS-MODIS_TERRA-fv2.0.nc')
        meta = dict()
        meta.update(self._attrs)
        meta.update(ds.attrs)
        coords = ('lon', 'lat', 'time')
        res = dict()
        for vs in ds.variables:
            if vs not in coords:
                if '_' not in vs:
                    if vs not in ('time', 'lat', 'lon'):
                        if 'standard_name' not in ds[vs]:
                            standard_name = vs
                        else:
                            standard_name = ds[vs].standard_name
                        meta_var = {'source_name':vs, 
                         'units':ds[vs].units, 
                         'long_name':ds[vs].long_name, 
                         'standard_name':standard_name, 
                         'valid_min':ds[vs].valid_min, 
                         'valid_max':ds[vs].valid_max}
                        meta_var.update(meta)
                        res[vs] = meta_var

        ds.close()
        return res

    def compute_source_time_ranges(self):
        from datetime import date, timedelta
        source_time_ranges = list()
        for root, sub_dirs, files in os.walk(self.dir_path):
            for file_name in files:
                if '.nc' in file_name:
                    f = os.path.join(root, file_name)
                    ds = netCDF4.Dataset(f)
                    t1 = ds.time_coverage_start
                    t1 = parse(t1).replace(tzinfo=None)
                    t2 = ds.time_coverage_end
                    t2 = parse(t2).replace(tzinfo=None)
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


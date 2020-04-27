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

class SSTProvider(CateCubeSourceProvider):

    def __init__(self, cube_config, name='sst', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    _attrs = {'title':'ESA SST CCI OSTIA L4 product', 
     'data_type': numpy.float64, 
     'fill_value': -9999, 
     'url':'http://www.esa-sst-cci.org', 
     'project':'Climate Change Initiative - European Space Agency', 
     'source_version':'v02.1', 
     'source_dir':'/neodc/esacci/sst/data/CDR_v2/Analysis/L4/v2.1'}

    @property
    def variable_descriptors(self):
        ds = xr.open_dataset('/neodc/esacci/sst/data/CDR_v2/Analysis/L4/v2.1/2010/01/01/20100101120000-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_CDR2.1-v02.0-fv01.0.nc')
        meta = dict()
        meta.update(self._attrs)
        meta.update(ds.attrs)
        coords = ('lon', 'lat', 'time')
        res = dict()
        for vs in ds.variables:
            if vs not in coords:
                if vs in ('analysed_sst', 'sea_ice_fraction', 'mask'):
                    if 'standard_name' not in ds[vs].attrs:
                        standard_name = vs
                    else:
                        standard_name = ds[vs].standard_name
                    meta_var = {'source_name':vs, 
                     #'long_name':ds[vs].long_name, 
                     #'standard_name':standard_name, 
                     #'valid_min':ds[vs].valid_min, 
                     #'valid_max':ds[vs].valid_max, 
                     'source':ds[vs].source}
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
                    t = file_name.split('-')
                    t = datetime.strptime(t[0], '%Y%m%d%H%M%S')
                    source_time_ranges.append((t, t, f, 0))

        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.flipud(source_image)

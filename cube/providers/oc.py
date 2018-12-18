import os
from datetime import datetime
from dateutil.parser import parse

import netCDF4
import numpy
import xarray as xr


from esdl.cate.cube_gen import CateCubeSourceProvider


class OCProvider(CateCubeSourceProvider):
    def __init__(self, cube_config, name='oc', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    _attrs = {"title": "ESA CCI Ocean Colour Product", 
                    'data_type': numpy.float32,
                    'fill_value': numpy.nan,
                    "url": "http://esa-oceancolour-cci.org",
                    "project": "Climate Change Initiative - European Space Agency", 
                    "source_version": "v3.1",
                    "source_dir": "/neodc/esacci/ocean_colour/data/v3.1-release/geographic/netcdf/chlor_a/daily/v3.1/",
                    }


    @property
    def variable_descriptors(self):
        ds = xr.open_dataset(self.dir_path + '/2012/ESACCI-OC-L3S-CHLOR_A-MERGED-1D_DAILY_4km_GEO_PML_OCx-20120101-fv3.1.nc')
        
        meta = dict()
        meta.update(self._attrs)
        meta.update(ds.attrs)

        res = dict()

        for vs in ds.variables:
            if vs == 'chlor_a':
                meta_var = ds[vs].attrs

                meta_var['source_name'] = vs

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
                    t = datetime.strptime(t[6], '%Y%m%d')

                    source_time_ranges.append((t, t, f, 0))
        
        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.flipud(source_image)


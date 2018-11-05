import os
from datetime import datetime

import numpy
import xarray as xr

from esdl.cate.cube_gen import CateCubeSourceProvider


class OzoneTemisProvider(CateCubeSourceProvider):
    def __init__(self, cube_config, name='ozone_temis', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    @property
    def variable_descriptors(self):
        shared_meta_info = {
                'data_type': numpy.float32,
                'fill_value': numpy.nan,
                'references': 'Jacob C. A. van Peet, Ronald J. van der A, Hennie M. Kelder, and Pieternel F. Levelt (2018),'
                                'Simultaneous assimilation of ozone profiles from multiple UV-VIS satellite instruments, Atmospheric Chemistry and Physics, '
                                'doi:10.5194/acp-18-1685-2018',
                'comment': 'The global tropospheric ozone column from 0 to 6 km is presented here. The column is derived by simultaneous assimlating ozone profiles of GOME-2 and OMI.',
                'url': 'http://www.temis.nl/protocols/tropo.html',
                'project_name' : 'Tropospheric ozone column',
        }

        ds = xr.open_dataset(self.dir_path + '/tropcol-20111202-v0002.nc')
        
        meta = dict()
        meta.update(shared_meta_info)
        meta.update(ds.attrs)

        coords = ('lon', 'lat', 'time')

        res = dict()

        for vs in ds.variables:
            if vs not in coords:
                meta_var = {
                                'source_name': vs,
                                'units': ds[vs].units,
                                'long_name': ds[vs].long_name,
                                'standard_name':  ds[vs].standard_name,
                                }
                meta_var.update(meta)
                res[vs] = meta_var
        ds.close()

        return res

    def compute_source_time_ranges(self):
        source_time_ranges = list()
        for root, sub_dirs, files in os.walk(self.dir_path):
            for file_name in files:
                if '.nc' in file_name:
                    f = os.path.join(root, file_name)

                    buff = file_name.split('-')
                    
                    dtt = datetime.strptime(buff[1], '%Y%m%d')
                    source_time_ranges.append((dtt, dtt, f, 0))

        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        # TODO (hans-permana, 20161219): the following line is a workaround to an issue where the nan values are
        # always read as -9.9. Find out why these values are automatically converted and create a better fix.
        source_image[source_image == -9.9] = numpy.nan
        return numpy.roll(numpy.flipud(source_image), 180, axis=1)

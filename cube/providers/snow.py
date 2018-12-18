import os
from datetime import datetime

import netCDF4
import numpy

from esdl.cate.cube_gen import CateCubeSourceProvider


class SnowProvider(CateCubeSourceProvider):
    def __init__(self, cube_config, name='snow', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    @property
    def variable_descriptors(self):
        return {
            'Band1': {
                    'long_name': 'GDAL Band Number 1',
                    'valid_range': '[  0 255]',
                    'grid_mapping': 'crs',
                    'GDAL_TIFFTAG_RESOLUTIONUNIT': '2',
                    'GDAL_TIFFTAG_XRESOLUTION': '72.0',
                    'GDAL_TIFFTAG_YRESOLUTION': '72.0',
                    'Conventions': 'CF-1.5',
                    'GDAL': 'GDAL 1.9.2, released 2012/10/08',
                    'source_name': 'Band1',
                    'data_type': numpy.float64,
                    'fill_value': None,
                    'units': 'unknown',
                    'standard_name': 'dry_atmosphere_mole_fraction_of_carbon_dioxide',
                    'url': 'http://icryoland.enveo.at/',
            }
        }

    def compute_source_time_ranges(self):
        from datetime import date, timedelta
        source_time_ranges = list()
        for root, sub_dirs, files in os.walk(self.dir_path):
            for file_name in files:
                if '.nc' in file_name:
                    f = os.path.join(root, file_name)

                    buff = file_name.split('_')
                    t1 = datetime.strptime(buff[2], '%Y%m%d%H%M')
                    t2 = datetime.strptime(buff[3], '%Y%m%d%H%M')

                    source_time_ranges.append((t1, t2, f, 0))

        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.flipud(source_image)

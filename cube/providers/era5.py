import esdl

import os
from datetime import timedelta

import netCDF4
import numpy
import datetime

from esdl.cube_provider import NetCDFCubeSourceProvider

all_descr = {
  "air_temperature_2m": { "air_temperature_2m" : {
                'source_name': 'air_temperature_2m',
                'data_type': numpy.float32,
                'fill_value': numpy.float32(-9999.0),
                'units': 'K',
                'long_name': '2 metre air temperature',
                'scale_factor': 1.0,
                'add_offset': 0.0,
                'references': '',
                'comment': 'Air temperature at 2m from the ERA5 reanalysis product.',
                'url': 'https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation',
                'project_name' : 'ERA5',
            }},
  "max_air_temperature_2m": { "max_air_temperature_2m": {
                'source_name': 'max_air_temperature_2m',
                'data_type': numpy.float32,
                'fill_value': numpy.float32(-9999.0),
                'units': 'K',
                'long_name': 'Maximum 2 metre air temperature',
                'scale_factor': 1.0,
                'add_offset': 0.0,
                'references': '',
                'comment': 'Air temperature at 2m from the ERA5 reanalysis product.',
                'url': 'https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation',
                'project_name' : 'ERA5',
            }},
  "min_air_temperature_2m": { "min_air_temperature_2m": {
                'source_name': 'min_air_temperature_2m',
                'data_type': numpy.float32,
                'fill_value': numpy.float32(-9999.0),
                'units': 'K',
                'long_name': 'Minimum 2 metre air temperature',
                'scale_factor': 1.0,
                'add_offset': 0.0,
                'references': '',
                'comment': 'Air temperature at 2m from the ERA5 reanalysis product.',
                'url': 'https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation',
                'project_name' : 'ERA5',
            }},
  "precipitation_era5": { "precipitation_era5": {
                'source_name': 'precipitation',
                'data_type': numpy.float32,
                'fill_value': numpy.float32(-9999.0),
                'units': 'K',
                'long_name': 'ERA 5 Precipitation',
                'scale_factor': 1.0,
                'add_offset': 0.0,
                'references': '',
                'comment': 'Total precipitation from the ERA5 reanalysis product.',
                'url': 'https://confluence.ecmwf.int//display/CKB/ERA5+data+documentation',
                'project_name' : 'ERA5',
            }},
}

class ERA5Provider(NetCDFCubeSourceProvider):
    def __init__(self, cube_config, dir, name="ERA5", resampling_order=None, varname=None):
        super(ERA5Provider, self).__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None
        self.varname=varname

    @property
    def variable_descriptors(self):
        return all_descr[self.varname]

    def compute_source_time_ranges(self):
        source_time_ranges = []
        file_names = filter(lambda x: x.endswith('nc'),os.listdir(self.dir_path))
        for file_name in file_names:
            file = os.path.join(self.dir_path, file_name)
            yr=int(file_name.split(".")[-2])
            d1=[datetime.datetime(yr,1,1)+datetime.timedelta(days=8*i) for i in range(46)]
            d2=[datetime.datetime(yr,1,9)+datetime.timedelta(days=8*i) for i in range(46)]
            d2[-1]=datetime.datetime(yr+1,1,1)
            source_time_ranges += [(d1[i], d2[i], file, i) for i in range(len(d1))]
        return sorted(source_time_ranges, key=lambda item: item[0])
      
    #def transform_source_image(self, source_image):
    #    """
    #    Transforms the source image, here by replacing NaNs with the missing value
    #    :param source_image: 2D image
    #    :return: source_image
    #    """
    #    source_image[numpy.isnan(source_image)] = self.missval
    #    return source_image

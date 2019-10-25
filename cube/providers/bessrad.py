import datetime
import os
from datetime import timedelta

import numpy

from esdl.cube_provider import NetCDFCubeSourceProvider

all_vars_descr = {'PAR': {
    'par': {
        'source_name': 'surface_downwelling_photosynthetic_radiative_flux_in_air',
        'data_type': numpy.float32,
        'fill_value': numpy.nan,
        'units': 'W m-2',
        'long_name': 'Photosynthetically active radiation',
        'standard_name': 'surface_downwelling_photosynthetic_radiative_flux_in_air',
        'url': 'http://environment.snu.ac.kr/bess_rad/',
        'references': 'Ryu, Y.*, Jiang, C., Kobayashi, H., & Detto, M. (2018).'
                      ' MODIS-derived global land products of shortwave radiation '
                      'and diffuse and total photosynthetically active radiation at '
                      '5 km resolution from 2000. Remote Sensing of Environment, 204, 812-825',
        'project_name' : 'BESS',
    }}, 'PARdiff': {
    'pardiff': {
        'source_name': 'surface_diffuse_downwelling_photosynthetic_radiative_flux_in_air',
        'data_type': numpy.float32,
        'fill_value': numpy.nan,
        'units': 'W m-2',
        'long_name': 'Diffuse Photosynthetically active radiation',
        'standard_name': 'surface_diffuse_downwelling_photosynthetic_radiative_flux_in_air',
        'url': 'http://environment.snu.ac.kr/bess_rad/',
        'references': 'Ryu, Y.*, Jiang, C., Kobayashi, H., & Detto, M. (2018).'
                      ' MODIS-derived global land products of shortwave radiation '
                      'and diffuse and total photosynthetically active radiation at '
                      '5 km resolution from 2000. Remote Sensing of Environment, 204, 812-825',
        'project_name' : 'BESS',
    }}, 'RSDN': {
    'Rg': {
        'source_name': 'surface_downwelling_shortwave_flux_in_air',
        'data_type': numpy.float32,
        'fill_value': numpy.nan,
        'units': 'W m-2',
        'long_name': 'Downwelling shortwave radiation',
        'standard_name': 'surface_downwelling_shortwave_flux_in_air',
        'url': 'http://environment.snu.ac.kr/bess_rad/',
        'references': 'Ryu, Y.*, Jiang, C., Kobayashi, H., & Detto, M. (2018).'
                      ' MODIS-derived global land products of shortwave radiation '
                      'and diffuse and total photosynthetically active radiation at '
                      '5 km resolution from 2000. Remote Sensing of Environment, 204, 812-825',
        'project_name' : 'BESS',
    }},
    

}


class BESSRadProvider(NetCDFCubeSourceProvider):
    def __init__(self, cube_config, name='BESSRad', dir=None, resampling_order=None, var=None):
        super(BESSRadProvider, self).__init__(cube_config, name, dir, resampling_order)
        self.var_name = var
        self.old_indices = None

    @property
    def variable_descriptors(self):
        return all_vars_descr[self.var_name]

    def compute_source_time_ranges(self):
        source_time_ranges = []
        file_names = filter(lambda x: x.endswith('nc'),os.listdir(self.dir_path))
        for file_name in file_names:
            file = os.path.join(self.dir_path, file_name)
            tspec = file_name.split(".")[-2]
            yr=int(tspec[1:5])
            d=int(tspec[5:])
            d1=datetime.datetime(yr,1,1)+datetime.timedelta(days=d-1)
            d2=d1+datetime.timedelta(days=1)
            source_time_ranges.append((d1, d2, file, 1))
        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by rotating and flipping.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.fliplr(numpy.rot90(source_image, 3))
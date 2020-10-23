import os
from datetime import datetime

import netCDF4
import numpy

from esdl.cate.cube_gen import CateCubeSourceProvider


class CH4Provider(CateCubeSourceProvider):
    def __init__(self, cube_config, name='xch4', dir=None, resampling_order=None):
        super().__init__(cube_config, name, dir, resampling_order)
        self.old_indices = None

    @property
    def variable_descriptors(self):
        return {
            'xch4': {
                'source_name': 'xch4',
                'data_type': numpy.float64,
                'fill_value': 1e+20,
                'units': '1',
                'cell_methods': 'time: mean',
                'long_name': 'column-average dry-air mole fraction of atmospheric carbon dioxide',
                'standard_name': 'dry_atmosphere_mole_fraction_of_carbon_dioxide',
                'references': 'Laeng, A., et al. "The ozone climate change initiative: Comparison of four '
                              'Level-2 processors for the Michelson Interferometer for Passive Atmospheric '
                              'Sounding (MIPAS)." Remote Sensing of Environment 162 (2015): 316-343.',
                'comment': 'Satellite retrieved column-average dry-air mole fraction of atmospheric carbon dioxide (XCO2)',
                'url': 'http://www.esa-ghg-cci.org/',
                'project_name' : 'Ozone CCI',
                'associated_files': 'obs4mips_co2_crdp3_v100.sav',
                'contact': 'maximilian.reuter@iup.physik.uni-bremen.de',
                'Conventions': 'CF-1.6',
                'creation_date': '20160303T111125Z',
                'data_structure': 'grid',
                'frequency': 'mon',
                'institute_id': 'IUP',
                'institution': 'Institute of Environmental Physics, University of Bremen',
                'mip_specs': 'CMIP5',
                'product': 'observations',
                'project_id': 'obs4MIPs',
                'realm': 'atmos',
                'source': 'ESA GHG CCI XCO2 CRDP3',
                'source_id': 'XCO2_CRDP3',
                'source_type': 'satellite_retrieval',
                'tracking_id': '60972082-05c2-4a04-947a-99042c642c68',
            }
        }

    def compute_source_time_ranges(self):
        from datetime import date, timedelta
        source_time_ranges = list()
        for root, sub_dirs, files in os.walk(self.dir_path):
            for file_name in files:
                if '.nc' in file_name:
                    f = os.path.join(root, file_name)
                    ds = netCDF4.Dataset(f)
                    base_date = date(1990, 1, 1)
                    time_index = 0
                    for time_bounds in ds.variables['time_bnds']:
                        time_start = timedelta(numpy.min(time_bounds))
                        time_end = timedelta(numpy.max(time_bounds))

                        time_start = base_date + time_start
                        time_end = base_date + time_end

                        time_start = datetime(time_start.year, time_start.month, time_start.day)
                        time_end = datetime(time_end.year, time_end.month, time_end.day)

                        source_time_ranges.append((time_start, time_end, f, time_index))
                        time_index += 1

                    ds.close()

        return sorted(source_time_ranges, key=lambda item: item[0])

    def transform_source_image(self, source_image):
        """
        Transforms the source image, here by flipping and then shifting horizontally.
        :param source_image: 2D image
        :return: source_image
        """
        return numpy.flipud(source_image)

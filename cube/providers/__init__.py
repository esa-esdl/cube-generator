"""
A list of available providers.
A provider is created for each input dataset so that an individual treatment in regards to data reading and
aggregation/interpolation can be applied.
"""

from .ozone import OzoneProvider
from .ch4 import CH4Provider
from .co2 import CO2Provider
from .aerosols import AerosolsProvider

__author__ = 'Brockmann Consult GmbH'

__all__ = [
    'OzoneProvider',
    'CH4Provider',
    'CO2Provider',
    'AerosolsProvider',
]

import os

try:
    import setuptools
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()

from setuptools import setup, find_packages


def get_version():
    version_file = 'version.py'
    locals = {}
    try:
        execfile(version_file, None, locals)
    except NameError:
        with open(version_file) as fp:
            exec(fp.read(), None, locals)
    return locals['version']


# Same effect as "from ect import __version__", but avoids importing ect:
__version__ = get_version()

# in alphabetical oder
requirements = [
    # Exclude 'gridtools' as it is only required for Cube production
    # 'gridtools',
    'numpy',
    'xarray',
]

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    # On READTHEDOCS, all dependencies are mocked (except tornado)
    # see doc/source/conf.py and readthedocs-env.yml
    requirements = ['gridtools']

packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name="cube-generation",
    version=__version__,
    description='ESDL Cube Software',
    license='GPL 3',
    author='ESDL Development Team',
    author_email='esdl@earthsystemdatacube.net',
    maintainer='Brockmann Consult GmbH',
    maintainer_email='admin@earthsystemdatalab.net',
    url='http://earthsystemdatalab.net/',
    packages=packages,
    entry_points={
        'esdl.source_providers': [
            'ozone_phi = cube.providers.ozone:OzoneProvider',
            'ozone_temis = cube.providers.ozone_temis:OzoneTemisProvider',
            'ch4 = cube.providers.ch4:CH4Provider',
            'co2 = cube.providers.co2:CO2Provider',
            'aerosol_phi = cube.providers.aerosols:AerosolsProvider',
            'sst = cube.providers.sst:SSTProvider',
            'oc = cube.providers.oc:OCProvider',
            'chlor_a = cube.providers.chlor_a:ChlorAProvider',
            'cloud = cube.providers.cloud:CloudProvider',
            'soil_moisture_esacci = cube.providers.soil_moisture_esacci:SoilMoistureESACCIProvider',
            'chirp = cube.providers.chirp:CHIRPProvider',
            'snow = cube.providers.snow:SnowProvider',
            'lc = cube.providers.lc:LCProvider',
            'par = cube.providers.par:ParProvider',
            'mld = cube.providers.mld:MldProvider',
            'bathy = cube.providers.bathy:BathyProvider',
            'pml1 = cube.providers.pml1:Pml1Provider',
            'pml2 = cube.providers.pml2:Pml2Provider',
            'pml3 = cube.providers.pml3:Pml3Provider',
            'pml4 = cube.providers.pml4:Pml4Provider',
            'pml5 = cube.providers.pml5:Pml5Provider',
            'pml6 = cube.providers.pml6:Pml6Provider',
            'pml7 = cube.providers.pml7:Pml7Provider',
            'pml8 = cube.providers.pml8:Pml8Provider',
            'pml9 = cube.providers.pml9:Pml9Provider',
            'pml10 = cube.providers.pml10:Pml10Provider',
            'pml11 = cube.providers.pml11:Pml11Provider',
            'pml12 = cube.providers.pml12:Pml12Provider',
        ],
    },
    # *Minimum* requirements
    install_requires=requirements
)

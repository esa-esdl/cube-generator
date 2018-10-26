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
            'ch4 = cube.providers.ch4:CH4Provider',
            'co2 = cube.providers.co2:CO2Provider',
        ],
    },
    # *Minimum* requirements
    install_requires=requirements
)

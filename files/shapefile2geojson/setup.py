from setuptools import setup, find_packages

setup(name='shapefile2geojson',
      version='0.1',
      description='Processor for converting Shapefiles to GeoJSON format',
      url='http://github.com/geoedf/shapefile2geojson',
      author='Rajesh Kalyanam',
      author_email='rkalyanapurdue@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['geopandas'],
      zip_safe=False)

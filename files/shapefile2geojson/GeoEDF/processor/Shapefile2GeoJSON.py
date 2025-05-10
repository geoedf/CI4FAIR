#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geoedfframework.utils.GeoEDFError import GeoEDFError
from geoedfframework.GeoEDFPlugin import GeoEDFPlugin

import geopandas as gpd
import glob
import os

""" Module for implementing the Shapefile2GeoJSON processor. This supports both a directory 
    of shapefiles (as a step in a workflow) and a single shapefile (when working on a locally 
    uploaded file). The resulting GeoJSON can be used in various map visualization libraries 
    like Folium or ipyLeaflet.
"""

class Shapefile2GeoJSON(GeoEDFPlugin):
    # input directory or shapefile params are XOR
    # shapefile will take precedence
    # if end is provided, period also needs to be provided
    __optional_params = ['inputdir','shapefile']
    __required_params = []

    # we use just kwargs since we need to be able to process the list of attributes
    # and their values to create the dependency graph in the GeoEDFPlugin super class
    def __init__(self, **kwargs):

        # list to hold all the parameter names; will be accessed in super to 
        # construct dependency graph
        self.provided_params = self.__required_params + self.__optional_params

        # check that all required params have been provided
        for param in self.__required_params:
            if param not in kwargs:
                raise GeoEDFError('Required parameter %s for Shapefile2GeoJSON not provided' % param)

        # specific check for conditionally required params
        # either inputdir or shapefile need to be provided
        # shapefile takes precedence
        if 'shapefile'not in kwargs and 'inputdir' not in kwargs:
            raise GeoEDFError('Either the inputdir or shapefile for Shapefile2GeoJSON need to be provided.')

        # set all required parameters
        for key in self.__required_params:
            setattr(self,key,kwargs.get(key))

        # set optional parameters
        for key in self.__optional_params:
            # if key not provided in optional arguments, defaults value to None
            setattr(self,key,kwargs.get(key,None))

        # class super class init
        super().__init__()

    # each Processor plugin needs to implement this method
    # if error, raise exception
    # assume this method is called only when all params have been fully instantiated
    def process(self):
        
        try:
            # if shapefile param has been provided, process just that one file
            if self.shapefile is not None:
                shpfile = gpd.read_file(self.shapefile)
                shpfile_basename = os.path.splitext(os.path.split(self.shapefile)[1])[0]
                geojson_filename = '%s/%s.json' % (self.target_path,shpfile_basename)
                shpfile.to_file(geojson_filename,driver='GeoJSON')
        
            # else, identify and process all shapefiles in inputdir
            shapefiles = glob.glob('%s/*.shp' % self.inputdir)
            for shapefile in shapefiles:
                shpfile = gpd.read_file(shapefile)
                shpfile_basename = os.path.splitext(os.path.split(shapefile)[1])[0]
                geojson_filename = '%s/%s.json' % (self.target_path,shpfile_basename)
                shpfile.to_file(geojson_filename,driver='GeoJSON')
        except:
            raise GeoEDFError('Error occurred when running Shapefile2GeoJSON processor')

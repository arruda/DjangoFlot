# -*- coding: utf-8 -*-

from django.core import serializers
from django.utils import simplejson
class teste(object):
    def __init__(self, datas=[],options=""):
        self.datas = datas
        self.options = options


        return simplejson.dumps(default=encode_myway,self)
            
def encode_myway(obj):
  if isinstance(obj, teste):
    return [obj.username,
            obj.firstname,
            obj.lastname,
            obj.email]
    # and/or whatever else
  elif isinstance(obj, OtherModel):
    return [] # whatever
  elif ...
  else:
    raise TypeError(repr(obj) + " is not JSON serializable")

class PlotData(object):
    """
    Contains the infos for each function represented in a plot.
    Has a data(coordinates list) and a option part referent to this data.
    """ 

    class PlotCoordinate(object):        
        def __init__(self, xAxis=[],yAxis=[]):
            self.xAxis = xAxis
            self.yAxis = yAxis 

    def __init__(self, datas=[],options=""):
        self.datas = datas
        self.options = options
    
    def __unicode__(self):
        return serializers.serialize("json",  self.datas)       
    

class PlotJson(object):
    """
    This is the final major plot class.
    """

    def __init__(self, datas=[],options=""):
        self.datas = datas
        self.options = options
    
    
        
        

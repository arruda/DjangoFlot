from DjangoFlot.plot.data.types import Lines, Points, Bars
    

class PlotData(object):
    """
    This class represents a plot data info.
    It has a list of data(infos for coordinate)
    
    """

    def __init__(self):        
        self.label = None
        #data = {}
        self.data = None
        self.lines = Lines
        self.points = Points        
        self.bars = Bars    
        
        #ints
        self.xaxis = None
        self.yaxis = None
        
    
#    def __unicode__(self):
#        return force_unicode(self.label)

    def printPlotData(self):
        #serialize DATA to JSON.
        return finalString
           

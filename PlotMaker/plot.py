
class PlotData(object):
    """
    This is a class that threats the plot data, that converts it to a string that JS can understand.
    """

    def __init__(self, xAxis=[], yAxis=[], label="label", plotType="lines", show=True, fill=True):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.label = label
        self.plotType = plotType
        self.show = show
        self.fill = fill
    
    
    def __unicode__(self):
        return force_unicode(self.label)

    def printPlotData(self):    
                     
        finalString = "{ label: \""+self.label+"\", "        
        finalString +="data: "
        finalString +="["
        maxAxis = max(len(self.xAxis),len(self.yAxis))   
        for i in xrange(maxAxis):
            finalString += "[" + str(self.xAxis[i]) + "," + str(self.yAxis[i])+"], "            
        finalString +="],"
        finalString +=self.plotType+": { show:"+str(self.show).lower()+", fill:"+str(self.fill).lower()+" }}"
        
        return finalString
           
        
def printSinglePlotData(plotData):    
                     
    finalString = "["+plotData.printPlotData()+"]"    

    return finalString  
    
def printMultiplesPlotDatas(plotDatas):    
                     
    finalString = "["
    for pd in plotDatas:
        finalString += pd.printPlotData()+","
    finalString += "]"    
    
    return finalString

        
     
        
        

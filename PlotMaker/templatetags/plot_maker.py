from django import template
from DjangoFlot.PlotMaker.plot import PlotData, printSinglePlotData, printMultiplesPlotDatas

register = template.Library()


@register.inclusion_tag('PlotMaker/tags/plotMakerTag.html')
def plotMaker(plotData,placeholder="placeholder",width="600",height="300"):    
        
    
    try:
        dataString = printMultiplesPlotDatas(plotData)            
    except TypeError: 
        dataString = printSinglePlotData(plotData)                          
                
    return {'datasets': dataString,'placeholder':placeholder,'width':width,'height':height,'plotData':plotData}


@register.inclusion_tag('PlotMaker/tags/plotMakerTag.html')
def multiplePlotsMaker(plotDatas,placeholder="placeholder",width="600",height="300"):  

    dataString = printMultiplesPlotDatas(plotDatas)               
        
                
    return {'datasets': dataString,'placeholder':placeholder,'width':width,'height':height}


# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from DjangoFlot.PlotMaker.models import *
from DjangoFlot.PlotMaker.plot import PlotData

def plot(request):
    
    listModels3 = Model3.objects.all()
    infos = []
    for md3 in listModels3:
    
        infos += [ [md3.xAxys , md3.yAxys] ]
    
    return render_to_response('index.html', {'infos':infos})
    
    
def teste(request):   
     
    listModels3 = Model3.objects.all()
        
    p1 = PlotData(xAxis = [], yAxis= [], label="Plot 1")    
    p2 = PlotData(xAxis = [], yAxis= [], label="Plot 2")  
    for md3 in listModels3:    
        p1.xAxis += [md3.xAxys]
        p1.yAxis += [md3.yAxys]
        p2.xAxis += [md3.yAxys]
        p2.yAxis += [md3.xAxys]
        
        
        
    plots = [p1,p2]    
        
    return render_to_response('index.html', {'p1': p1,'p2':p2,'plots':plots})
    #return render_to_response('index.html', {'p1': p1})
    

# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from DjangoFlot.PlotMaker.models import *


def plot(request):
    
    listModels3 = Model3.objects.all()
    infos = []
    for md3 in listModels3:
    
        infos += [ [md3.xAxys , md3.yAxys] ]
    
    return render_to_response('index.html', {'infos':infos})
    
    
def teste(request):    
    return render_to_response('PlotMaker/index.html')

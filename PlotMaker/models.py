# -*- coding: utf-8 -*-

from django.db import models

    
    

    
class Model3(models.Model):
    name = models.CharField(u"Name",unique=True,max_length=14)
    xAxys =  models.IntegerField(u"X Axys Value")   
    yAxys =  models.IntegerField(u"Y Axys Value")   
    models.IntegerField(u"value")   
    #models1 = models.ManyToManyField(Model1)
    #models2 = models.ManyToManyField(Model2)

    
    def __unicode__(self):
        return self.name

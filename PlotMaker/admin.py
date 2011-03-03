from django.contrib import admin
from DjangoFlot.PlotMaker.models import Model3





class Model3Admin(admin.ModelAdmin):
    fieldsets = [
           ('Model',               {'fields': ['name','xAxys','yAxys']}),
    ]

    list_display = ('name','xAxys','yAxys',)



admin.site.register(Model3, Model3Admin)

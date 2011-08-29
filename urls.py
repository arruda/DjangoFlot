from django.conf.urls.defaults import *

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # (r'^DjangoFlot/', include('DjangoFlot.foo.urls')),
    

    (r'^admin/', include(admin.site.urls)),
    #(r'^$', direct_to_template, {'template':'index.html','dados':dados}),
    #(r'^$', 'DjangoFlot.PlotMaker.views.teste'),
    #(r'^$', 'DjangoFlot.PlotMaker.views.teste'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

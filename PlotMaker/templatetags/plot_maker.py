from django import template

#using this to get the FLOT_JS_MEDIA from settings.
#from django.conf import settings

register = template.Library()


@register.inclusion_tag('tags/plotMakerTag.html')
def plotMaker(data):
    return {'data': data}


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# load the geoip, so that we can detect user's location based on their ip address
# from django.contrib.gis.geoip import GeoIP
# load the 3rd library for detecting user's ip address
from ipware.ip import get_ip

def index(request):
  user_ip = get_ip(request)
  template = loader.get_template('index.html')
  context = {
    'name' : 'name from controller',
    # 'request' : g.city('72.14.207.99'),
  }
  return HttpResponse(template.render(context, request))

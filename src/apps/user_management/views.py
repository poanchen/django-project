from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# http://127.0.0.1:8000/user
# http://127.0.0.1:8000/user/
def user(request):
  template = loader.get_template('index.html')
  context = {
    'name' : 'yo from user controller haha',
  }
  return HttpResponse(template.render(context, request))

# http://127.0.0.1:8000/user/login
# http://127.0.0.1:8000/user/login/
def login(request):
  template = loader.get_template('index.html')
  context = {
    'name' : 'yo from login controller',
  }
  return HttpResponse(template.render(context, request))

# http://127.0.0.1:8000/user/register
# http://127.0.0.1:8000/user/register/
def register(request):
  template = loader.get_template('index.html')
  context = {
    'name' : 'yo from register controller',
  }
  return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import upload

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

# http://127.0.0.1:8000/user/[A-Za-z0-9]
# http://127.0.0.1:8000/user/[A-Za-z0-9]/
# for example, http://127.0.0.1:8000/user/edfc4c8f3e
# for example, http://127.0.0.1:8000/user/edfc4c8f3e/
# In full name, it will be
# http://127.0.0.1:8000/user/[A-Za-z0-9]/firstname-lastname
# http://127.0.0.1:8000/user/[A-Za-z0-9]/firstname-lastname/
# for example, http://127.0.0.1:8000/user/edfc4c8f3e/firstname-lastname
# for example, http://127.0.0.1:8000/user/edfc4c8f3e/firstname-lastname/
def user(request):
  template = loader.get_template('user.html')
  path = request.path
  splittedPath = path.split('/')
  user_id = splittedPath[2]
  person = upload.get_user_meta_data(user_id)

  if person is None:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request))
  else:
    context = {
      'person' : person
    }
    return HttpResponse(template.render(context, request))
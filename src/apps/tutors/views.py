from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.utils.module_loading import import_module

# http://127.0.0.1:8000/tutors
# http://127.0.0.1:8000/tutors/
def search(request):
  template = loader.get_template('search.html')
  apps = import_module('apps.user_management')
  param = retrieve_all_get_parameters(request)
  tutors = apps.upload.get_list_of_tutors(param)

  # for x in range(len(tutors)):
  #   apps.upload.create_user_folder(tutors[x]['user_id'])

  context = {
    'prices' : ['No limit', 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'locations' : ['Not specified', 'Florida, BD', 'Washington, DC', 'New York, AB', 'Los Angles, BT', 'Victoria, BC'],
    'tutors' : tutors,
  }
  return HttpResponse(template.render(context, request))

def retrieve_all_get_parameters(request):
  param = {}
  q = request.GET.get('q')
  m_p = request.GET.get('m_p')
  l = request.GET.get('l')

  if q != None and q != '':
    param['q'] = q
  if m_p != None and m_p != '':
    param['m_p'] = m_p
  if l != None and l != '':
    param['l'] = l

  return param
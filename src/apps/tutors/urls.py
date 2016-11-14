from django.conf.urls import url

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/tutors
  # http://127.0.0.1:8000/tutors/
  url(r'/?', views.search, name='search'),
]
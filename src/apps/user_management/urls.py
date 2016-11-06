from django.conf.urls import url

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/user
  # http://127.0.0.1:8000/user/
  url(r'^/?$', views.user, name='user'),
  # http://127.0.0.1:8000/user/login
  # http://127.0.0.1:8000/user/login/
  url(r'login/?', views.login, name='login'),
  # http://127.0.0.1:8000/user/register
  # http://127.0.0.1:8000/user/register/
  url(r'register/?', views.register, name='register'),
]
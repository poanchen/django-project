from django.conf.urls import url

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/user/login
  # http://127.0.0.1:8000/user/login/
  url(r'login/?', views.login, name='login'),
  # http://127.0.0.1:8000/user/register
  # http://127.0.0.1:8000/user/register/
  url(r'register/?', views.register, name='register'),
  # http://127.0.0.1:8000/user/[A-Za-z0-9]
  # http://127.0.0.1:8000/user/[A-Za-z0-9]/
  # for example, http://127.0.0.1:8000/user/edfc4c8f3e
  # for example, http://127.0.0.1:8000/user/edfc4c8f3e/
  # In full name, it will be
  # http://127.0.0.1:8000/user/[A-Za-z0-9]/firstname-lastname
  # http://127.0.0.1:8000/user/[A-Za-z0-9]/firstname-lastname/
  # for example, http://127.0.0.1:8000/user/edfc4c8f3e/firstname-lastname
  # for example, http://127.0.0.1:8000/user/edfc4c8f3e/firstname-lastname/
  url(r'[\w]/?', views.user, name='user'),
]
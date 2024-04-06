from django.urls import path
from . import views
from .views import login_view, signup_view

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('login/', views.login_view, name='login'),
path('signup/', views.signup_view, name='signup'),
]

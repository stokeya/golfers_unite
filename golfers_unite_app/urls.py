from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import login_view, signup_view, add_scorecard
from django.contrib import admin
from django.urls import reverse_lazy

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('admin/', admin.site.urls),
path('golfers_unite_app/login/', LoginView.as_view(template_name='login.html'), name='login'),
path('golfers_unite_app/signup/', views.signup_view, name='signup'),
path('golfers_unite_app/active-golfers/', views.active_golfers_view, name='active_golfers'),
path('golfers_unite_app/add_scorecard/<int:golfer_id>/', views.add_scorecard, name='add_scorecard'),
path('golfers_unite_app/delete-scorecard/<int:scorecard_id>/', views.delete_scorecard, name='delete_scorecard'),
path('golfers_unite_app/search_golf_courses/', views.search_golf_courses, name='search_golf_courses'),
]

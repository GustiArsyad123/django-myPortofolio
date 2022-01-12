from django.urls import path
#import views
from . import views

urlpatterns = [
     #add this code
     path('', views.home, name='home'),
     path('about', views.about, name='about')
]
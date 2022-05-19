from django.urls import path 
from . import views
urlpatterns = [
 path('', views.index),
 path('add_dojo', views.Dojo),
 path('add_ninja', views.Ninja),
 path('delete', views.delete),
]
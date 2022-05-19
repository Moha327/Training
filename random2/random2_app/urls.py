from django.urls import path 
from . import views
urlpatterns = [
  path('', views.a),
  path('check', views.index),
  path('again', views.delete),
]
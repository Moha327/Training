from django.urls import path 
from . import views
urlpatterns = [
 path('shows', views.index),
 path('create_shows', views.create_shows),
 path('shows/<int:number>',views.some_shows),
 path('shows/<int:number>/edit',views.some_update),
 path('shows/new',views.index2),
 path('Update',views.Update),
 path('shows/<int:number>/delete',views.Delete)
]
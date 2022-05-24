from django.urls import path 
from . import views
urlpatterns = [
 path('', views.index),
 path('wall',views.index2),
 path('register',views.create_user),
 path('login',views.loginProcess),
 path('logout',views.logout),
 path('posted',views.create_message),
 path('comment',views.create_comment),
 path('delete_process',views.delete_process),
]
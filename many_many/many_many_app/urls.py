from django.urls import path 
from . import views
urlpatterns = [
 path('', views.index),
 path('add_book',views.create_books_db),
 path('books/<int:number>',views.book),
 path('authors',views.index2),
 path('add_author',views.create_authors_db),
 path('authors/<int:Num>',views.books),
path('some_book',views.some_book),
]
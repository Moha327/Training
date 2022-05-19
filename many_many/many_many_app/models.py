from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes=models.TextField(blank=True)
    books = models.ManyToManyField(books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def books_db():
    return books.objects.all()
def create_books_db(title,desc):
    return books.objects.create(title=title,desc=desc)
def authors_db():
    return authors.objects.all()
def create_authors_db(first_name,last_name,notes):
    return authors.objects.create(first_name=first_name,last_name=last_name,notes=notes)
def some_authors(Num):
    return authors.objects.get(id=Num)
def some_book(number):
    return books.objects.get(id=number)
def assign_authors(book_id,assigned_author):
    return books.objects.get(id=book_id).authors.add(assigned_author)
def assign_books(author_id,assigned_book):
    return authors.objects.get(id=author_id).books.add(assigned_book)
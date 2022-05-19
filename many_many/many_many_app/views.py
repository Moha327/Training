from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from . import models
def index(request):
    context={
        "books":models.books_db(),
    }
    return render(request,"index.html",context)
def create_books_db(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        models.create_books_db(title,desc)
        return redirect('/')
    else:
        return HttpResponse('No way')
def book(request,number):
    context={
        'Some_Book':models.some_book(number),
        'authors':models.authors_db()
    }
    return render(request,'index3.html',context)
def index2(request):
    context={
        "authors":models.authors_db(),
    }
    return render(request,"index2.html",context)
def create_authors_db(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        notes=request.POST['notes']
        models.create_authors_db(first_name,last_name,notes)
        return redirect('/authors')
    else:
        return HttpResponse('No way')
def books(request,Num):
    context={
        'Some_Author':models.some_book(Num),
        'books':models.books_db(),
        'author_id':Num
    }
    return render(request,'index4.html',context)
def some_book(request):
    if request.method=="POST":
        assigned_author=request.POST["assigned_author"]
        book_id=request.POST["book_id"]
        models.assign_authors(book_id,assigned_author)
        return redirect("/books/"+book_id)
    else:
        return HttpResponse("You aren't allowed to manually adjust the URL!")
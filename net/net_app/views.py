from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render, HttpResponse,redirect
from . import models
from django.contrib import messages
from .models import Show
def index(request):
    context={
        'all_shows':models.show_db()
    }
    return render(request,"index.html",context)
def index2(request):
    return render(request,'index2.html')
def create_shows(request):
    if request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['released_date']
        description=request.POST['description']
        models.create_shows(title,network,release_date,description)
        return redirect('/shows/'+str(models.get_show_id(title)))
def some_shows(request,number):
    context={
        'Some_Show':models.some_show(number),
        'num':number
    }
    return render(request,'index4.html',context)
def some_update(request,number):
    context={
        'Some_Show':models.some_show(number),
        'num':number
    }
    return render(request,'index3.html',context)
def Update(request):
    if request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/'+str(request.POST['show_id_grabber'])+'/edit')
    else:
        id=request.POST['show_id_grabber']
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['released_date']
        description=request.POST['description']
        models.update(id,title,network,release_date,description)
        return redirect('/shows/'+str(id))
def Delete(request,number):
    models.delete(number)
    return redirect('/shows')
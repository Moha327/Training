from django.shortcuts import render, redirect,HttpResponse
from . import models
def index(request):
    context={
        "Dojos":models.show_dojos()
    }
    return render(request,'index.html',context)

def Dojo(request):
    if request.method=='POST':
        dojo_name=request.POST['name']
        dojo_city=request.POST['city']
        dojo_state=request.POST['state']
        models.dojos_db(dojo_name,dojo_city,dojo_state)
        return redirect('/')
    else:
        return HttpResponse("You are not allowed to change the route manually!")
def Ninja(request):
    if request.method=='POST':
        ninja_first_name=request.POST['first_name']
        ninja_last_name=request.POST['last_name']
        ninja_author=request.POST['author']
        models.ninjas_db(ninja_first_name,ninja_last_name,ninja_author)
        return redirect('/')
    else:
        return HttpResponse("You are not allowed to change the route manually!")
def delete(request):
    if request.method=='POST':
        id=request.POST['id']
        models.Delete(id)
        return redirect('/')

#from django.shortcuts import render,HttpResponse,redirect
#from . import models
#from .models import Show

#def root(request):
 #   return redirect('/shows')
#def index(request):
#    return render(request,'index.html')
#def add_show(request):
#    if request.method=="POST":
#        title=request.POST['title']
 #       network=request.POST['network']
 #       release_date=request.POST['release_date']
 #       description=request.POST['description']
 #       models.add_show(title,network,release_date,description)
#        return redirect('/shows/'+str(models.get_show_id(title)))
#    else:
#        return HttpResponse('pleplfplplefeplplfplf')
#def index2(request):
#    context={
 #       "shows":models.show()
 #   }
 #   return render(request,'index2.html',context)
#def index3(request):
#    return render(request,'index3.html')
#def index4(request,id):
#    context={
 #       "Some_Show":models.some_show(id),
 #       "num":id
 #   }
 #   return render(request,'index4.html')
#def update_show_process(request):
 #   if request.method=="POST":
 #       id=request.POST["id"]
 #       title=request.POST["title"]
 #       network=request.POST["network"]
 #       release_date=request.POST["release_date"]
 #       description=request.POST["description"]
 #       models.update(id,title,network,release_date,description)
#        return redirect("/shows/"+str(id))
#    else:
#        return HttpResponse("You can't manually change the URL!")
#def delete(request,number):
 #   models.delete(number)
 #   return redirect("/")
from django.shortcuts import render,HttpResponse,redirect
from . import models
from .models import Show

def root(request):
    return redirect("/shows")

def shows(request):
    context={
        "All_Shows":models.all_shows(),
    }
    return render(request,"shows.html",context)


def add_shows(request):
    return render(request,"add_shows.html")


def create_shows(request):
    if request.method=="POST":
        show_title=request.POST["show_title"]
        show_network=request.POST["show_network"]
        show_release_date=request.POST["show_release_date"]
        show_description=request.POST["show_description"]
        models.add_shows(show_title,show_network,show_release_date,show_description)
        return redirect("/shows/"+str(models.get_show_id(show_title)))
    else:
        return HttpResponse("You can't manually change the URL!")

def some_show(request,number):
    context={
        "Some_Show":models.some_show(number),
        "NUM":number,
        }
    return render(request,"some_show.html",context)

def update_show(request,number):
    context={
        "Some_Show":models.some_show(number),
        "NUM":number,
    }
    return render(request,"update_show.html",context)

def update_show_process(request):
    if request.method=="POST":
        show_id=request.POST["show_id_grabber"]
        show_title=request.POST["show_title"]
        show_network=request.POST["show_network"]
        show_release_date=request.POST["show_release_date"]
        show_description=request.POST["show_description"]
        models.update(show_id,show_title,show_network,show_release_date,show_description)
        return redirect("/shows/"+str(show_id))
    else:
        return HttpResponse("You can't manually change the URL!")

def delete(request,number):
    models.delete(number)
    return redirect("/")
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from . import models
def index(request):
    context={
        "User":models.show_users()
    }
    return render(request,'index.html',context)
def create_user(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email_address=request.POST['eaddress']
        age=request.POST['age1']
        models.create_user(first_name,last_name,email_address,age)
        return redirect('/')
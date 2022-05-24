from django.shortcuts import render,HttpResponse,redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'index.html')
def index2(request):
    if "id" in request.session:
        context={
            'All_message':models.display_all_messages()
        }
        return render(request,"index2.html",context)

def create_user(request):
    errors = User.objects.validator(request.POST)
    if request.method=="POST" :
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_pw=request.POST["confirm_pw"]
        birthday=request.POST["date"]
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            if models.check_email(email=email)==False:
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
                user=models.register(first_name,last_name,email,hashed_pw,birthday)
                request.session["id"]=user.id
                request.session["FIRSTNAME"]=user.first_name
                request.session["LASTNAME"]=user.last_name
                request.session["EVENT"]="registered"
            return redirect('/wall')
    else:
        return HttpResponse("You are not allowed to manually change the URL!")
def loginProcess(request):
    if request.method=="POST":
        username=request.POST["username"]
        userpw=request.POST["userpw"]
        user=models.login_username(username)
        if user and bcrypt.checkpw(userpw.encode(), user.password.encode()):
            request.session["id"]=models.get_user_id(username)
            request.session["FIRSTNAME"]=models.get_first_name(username)
            request.session["LASTNAME"]=models.get_last_name(username)
            request.session["EVENT"]="logged in"
            return redirect("/wall")
        else:
            return HttpResponse("Log in information didn't match!")
    else:
        return HttpResponse("You are not allowed to manually change the URL!")
def logout(request):
    request.session.flush()
    return redirect("/")
def create_message(request):
    if request.method=='POST':
        message=request.POST['message']
        user_id=request.POST['user_id']
        models.create_message(message,user_id)
        return redirect('/wall')
def create_comment(request):
    if request.method=="POST":
        comment=request.POST["comment"]
        user_id=request.session["id"]
        msg_id=request.POST["msg_id"]
        models.create_comment(comment,user_id,msg_id)
        return redirect("/wall")
    else:
        return HttpResponse("You are not allowed to manually change the URL!")
def delete_process(request):
    if request.method=="POST":
        message_id=request.POST["messageID"]
        models.delete_a_post(message_id)
        return redirect("/wall") 
    else:
        return HttpResponse("You are not allowed to manually change the URL!")
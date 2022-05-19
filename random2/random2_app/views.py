from django.shortcuts import redirect, render, HttpResponse
import random
def a(request):
    if "random" not in request.session:
        request.session["random"]=random.randint(1, 100)
        request.session["again"]="hidden"
    return render(request,'index.html')
def index(request):
    if int(request.POST['random1'])==request.session['random']:
        request.session["style"]="won"
        request.session["content"]=f"{request.session['random']} was the number"
        request.session["again"]="submit"
        return redirect('/')
    elif int(request.POST["random1"])>request.session["random"]:
                request.session["content"]="Too high!"
                request.session["again"]="hidden"
                return redirect('/')
    elif int(request.POST["random1"])<request.session["random"]:
                request.session["content"]="Too low!"
                request.session["again"]="hidden"
                return redirect('/')
def delete(request):
    request.session["style"]="hiddenDIV"
    request.session["again"]="hidden"
    del request.session["content"]
    del request.session["random"]
    return redirect('/')
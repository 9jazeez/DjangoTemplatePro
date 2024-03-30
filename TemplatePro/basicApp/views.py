from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello World!")
    cont_dic = {"text": 'hello world', "text2": 'good morning'}
    return render(request, "basicApp/index.html", cont_dic)

def home(request):
    return render(request, "basicApp/home.html")

def help(request):
    return render(request, "basicApp/help.html")

def base(request):
    return render(request, "basicApp/base.html")

# Create your views here.

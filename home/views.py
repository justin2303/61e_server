from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"home/index.html")

def Events(request):
    return render(request,"home/Events.html")

def Chvls(request):
    return render(request,"home/chvls.html")

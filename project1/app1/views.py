from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,"app1/base.html")



# Create your views here.

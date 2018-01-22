from django.shortcuts import render
from analysis.models import textarea
from . import rake1




def home(request):
    return render(request,"index.html")


def try_it(request):
    return render(request,"try_it.html")




def try1(request):
    return render(request,"try1.html")




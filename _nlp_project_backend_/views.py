from django.shortcuts import render
from analysis.models import textarea

def home(request):
    return render(request,"index.html")


def try_it(request):
    return render(request,"try_it.html")



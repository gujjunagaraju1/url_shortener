from django.shortcuts import render,redirect
import string
import random
from .models import UrlData
from django.contrib import messages


def home(request):
    if request.method=="POST":
        original=request.POST.get('url')
        obj=UrlData.create(original)
        return render(request,'home.html',{
            'full_url':obj.original,
            'short_url':request.get_host()+'/'+obj.short,
        })
    
    return render(request,'home.html')

def router(request,key):
    try:
        obj=UrlData.objects.get(short=key)
        return redirect(obj.original)
    except:
        return redirect(home)


# Create your views here.

# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django import forms 
from django.http.response import HttpResponse
import datetime
from models import Book
from models import Publisher
from models import Author
# Create your views here.

class VMform(forms.Form):
    name = forms.CharField()
    memory = forms.CharField()
    disk = forms.CharField()
    ni = forms.BooleanField()
 
   

def create(req):
    if req.method=="POST":
        form = VMform(req.POST)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponse("ok")
    
    
    else:
        form = VMform()
    return render_to_response("create.html",{"form":form})# 


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('currenttime.html', locals())

def current_hour(request):
    current_hour = "don not know "
    return render_to_response('hoursahead.html', {"hour_offset":current_hour})           

def bookshow(request):
    #Autor.objects.create("first_name"='zhang','last_name'='wang','email'='lisiwobushi@qq.com')
    au = Author()
    au.first_name='zhang'
    au.last_name = 'er'
    au.email = 'www.qq.com'
    au.save()
    
    authorlist = Author.objects.all()
    return render_to_response('bookpage.html',{"author":au,'authorlist':authorlist})

    

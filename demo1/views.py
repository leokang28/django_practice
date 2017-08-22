from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(req):
  demo = models.demo.objects.get(pk=1)
  return render(req,'index.html',{
    'demo':demo
  })
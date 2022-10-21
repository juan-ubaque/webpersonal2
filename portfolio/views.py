from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio (request):
    projects = Project.objects.all() #devuleve todos losobjetos del projecto
    return  render (request,'Tportfolio/portfolio.html',{'projects':projects})

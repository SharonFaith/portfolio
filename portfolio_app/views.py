from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import requests
from .models import Project
#from .forms import 
from django.contrib.sites.shortcuts import get_current_site
import random




def index(request):
   

   return render(request, 'index.html')

def projects(request):

   listed_projects = Project.objects.all()

   return render(request, 'projects.html', {'projects': listed_projects})
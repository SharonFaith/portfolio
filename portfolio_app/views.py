from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import requests
#from .models import 
#from .forms import 
from django.contrib.sites.shortcuts import get_current_site
import random




def index(request):
   

   return render(request, 'index.html')


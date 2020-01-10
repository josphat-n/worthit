from django.shortcuts import render
from django.http  import HttpResponse
from .forms  import ProjectForm
# Create your views here.

def home(request):
   return render(request, 'rate/home.html')

def project(request):
   form = ProjectForm()
   
   return render(request, 'rate/new-project.html', {"prjForm": form})
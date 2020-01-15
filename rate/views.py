from django.shortcuts import render
from django.http  import HttpResponse
from .forms  import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
   return render(request, 'rate/home.html')

@login_required(login_url='/accounts/login/')
def project(request):
   form = ProjectForm()
   
   return render(request, 'rate/new-project.html', {"prjForm": form})

def profile(request):
   
   return render(request, 'profile/profile.html')
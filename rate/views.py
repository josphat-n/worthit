from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .forms  import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
   return render(request, 'rate/home.html')

@login_required(login_url='/accounts/login/')
def project(request):
   current_user = request.user
   if request.method == 'POST':
      form = ProjectForm(request.POST, request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.save()
      return redirect('/profile')
   else:
      form = ProjectForm()   
   return render(request, 'rate/new-project.html', {"form": form})

def profile(request):
   
   return render(request, 'profile/profile.html')
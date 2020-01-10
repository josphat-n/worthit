from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
   path('', views.home, name ='worthit-home'),
   path('project/', views.project, name="new-project"),
]  
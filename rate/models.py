from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   name = models.ForeignKey(User,on_delete=models.CASCADE)
   picture = ImageField(blank=True, manual_crop="")
   bio = models.TextField()   
   contact = models.CharField(max_length =30)
   
   def __str__(self):
      return self.name
   
   @classmethod
   def get_all(cls):
      """
      This function allows for the fetching of all the profile objects from the database
      """
      prof = Profile.objects.all()
      return prof
   def save_profile(self):
      """
      Save a profile to the database    
      """
      self.save()   
   
   def delete_profile(self):
      """
      function to delete a profile from the db
      """
      self.delete()   
   
class Project(models.Model):
   title = models.CharField(max_length =30)
   poster = ImageField(blank=True, manual_crop="")
   description = models.TextField()
   live_link = models.CharField(max_length = 50)
   posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE, default = 1)
   
   def __str__(self):
      return self.title
   
   @classmethod
   def get_all(cls):
      """
      This function allows for the fetching of all the project objects from the database
      """
      projs = Project.objects.all()
      return projs 
      

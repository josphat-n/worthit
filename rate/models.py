from django.db import models

# Create your models here.
class Profile(models.Model):
   # picture = ImageField(blank=True, manual_crop="")
   bio = models.TextField()   
   contact = models.CharField(max_length =30)
   
class Project(models.Model):
   title = models.CharField(max_length =30)
   # image = ImageField(blank=True, manual_crop="")
   description = models.TextField()
   live_link = models.CharField(max_length = 50)
   posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE, default = 1)
   
   def __str__(self):
      return self.title

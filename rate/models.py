from django.db import models

# Create your models here.
class Project(models.Model):
   title = models.CharField(max_length =30)
   # image = ImageField(blank=True, manual_crop="")
   description = models.TextField()
   live_link = models.CharField(max_length = 50)
   
   def __str__(self):
      return self.title
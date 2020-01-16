from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
   # Setup Method
   def setUp(self):
      # self.name=User(id = 1)
      self.profile_one=Profile(bio= 'A cool dude', name_id=1, contact = '0731-633511')
      
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.profile_one,Profile))      
      
   # Testing Save Method
   def test_save_method(self):
      self.profile_one.save_profile()
      prof = Profile.objects.all()
      self.assertTrue(len(prof) > 0)     
      
   # Teardown Method
   def tearDown(self):
      Profile.objects.all().delete()           
   
   #Delete Method   
   def test_delete(self):
      self.profile_one.save_profile()    
      self.profile_one.delete_profile()
      prof = Profile.objects.all()
      self.assertTrue(len(prof)<1)            
      
class ProjectTestClass(TestCase):
   # Setup Method
   def setUp(self):
      self.profile=Profile(id = 1)
      self.project_one=Project(title='git-search',description='Consumes the github API and allows serches in github',live_link= 'httpsa://gitthub.com/Josephat-n/gitSearch') 
      
   # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.project_one,Project))  
      
   # Testing Save Method
   def test_save_method(self):
      self.project_one.save_project()
      projs = Project.objects.all()
      self.assertTrue(len(projs) > 0)       
   # Teardown Method
   def tearDown(self):
      Project.objects.all().delete()    
       
   #Delete Method   
   def test_delete(self):
      self.project_one.save_project()    
      self.project_one.delete_project()
      projs = Project.objects.all()
      self.assertTrue(len(projs)<1)      
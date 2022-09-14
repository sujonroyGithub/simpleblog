
from django.utils import timezone
from operator import mod
from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to="app/images", default="" )
    date = models.DateField()
    
    # author=models.ForeignKey(User)
    
 

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name 
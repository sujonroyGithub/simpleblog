from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to="app/images", default="" )

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name 
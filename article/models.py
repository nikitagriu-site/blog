from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255) # CharField = Character Field
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=255) 
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

    
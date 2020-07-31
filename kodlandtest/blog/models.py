from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title 		= models.CharField(max_length=200, unique=True)
    updated_on 	= models.DateTimeField(auto_now= True)
    content 	= models.TextField()
    created_on 	= models.DateTimeField(auto_now_add=True)
    image 		= models.ImageField(upload_to='post')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
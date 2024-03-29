from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# This is mode for the post articale
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # imges = models.ImageField(null=True, blank=True)
    image = models.ImageField(default='1200x-1.jpeg', upload_to='profile_pics')
    
   
    

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    


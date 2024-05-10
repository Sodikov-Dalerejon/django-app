from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=False)
    image=models.ImageField(upload_to="images/", blank=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("admin", args=[str(self.pk)])
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
	
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True)
	technology = models.CharField(max_length=20)
	image = models.ImageField(upload_to='images')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	
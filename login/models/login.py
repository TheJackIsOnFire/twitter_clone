from django.db import models
from django.contrib.auth.models import AbstractUser

class Login(models.Model):
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    data_time = models.DateTimeField(auto_now_add=True)
from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
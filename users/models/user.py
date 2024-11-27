from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=254)
    username = models.CharField(max_length=254, unique=True, default="@username")
    email = models.EmailField(max_length=254, unique=True, default="xxx@email.com")
    password = models.CharField(max_length=254)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
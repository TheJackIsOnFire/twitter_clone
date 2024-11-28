from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=254, default="@fullname")
    username = models.CharField(max_length=254, unique=True, default="@username")
    email = models.EmailField(max_length=254, unique=True, default="xxx@email.com")
    password = models.CharField(max_length=254)

    def __str__(self):
        return self.username
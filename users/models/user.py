from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=254)
    username = models.CharField(max_length=254, unique=True, error_messages={'unique': "O username cadastrado já existe."}, default="@username")
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."}, default="xxx@email.com")
    password = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
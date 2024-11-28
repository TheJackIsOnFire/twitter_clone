# Django model for blog post and users authentication
from django.db import models
from users.models.user import User

status = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    id =  models.AutoField(primary_key=True)
    title = models.CharField(max_length=254, unique=True) # title of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_tweets') # author of the post via foreign key
    updated_on = models.DateTimeField(auto_now=True) # last updated date
    content = models.TextField() # content of the post
    created_on = models.DateTimeField(auto_now_add=True) # created date
    status = models.IntegerField(choices=status, default=0) # status of the post

    class Meta: # meta class for ordering the posts by created date
        ordering = ['created_on'] # order by created date


    def __str__(self): # string representation of the post
        return self.title # return the title of the post

from django.db import models

from .user import User

class UserConnections(models.Model):
    user_main = models.ForeignKey(User, related_name="user_main_set", on_delete=models.CASCADE, null=True, blank=True, default='@user')
    followed = models.ForeignKey(User, related_name="followed_set", on_delete=models.CASCADE, null=True, blank=True, default='@followed')
    follower = models.ForeignKey(User, related_name="follower_set", on_delete=models.CASCADE, null=True, blank=True, default='@follower')
    data_time = models.DateTimeField(auto_now_add=True)

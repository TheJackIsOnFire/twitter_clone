from django.db import models

from .user import User

class UserConnections(models.Model):
    main_user = models.OneToOneField(User, related_name="main_user", on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name="followed_set", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="following_set", on_delete=models.CASCADE)

    def __str__(self):
        return self.main_user
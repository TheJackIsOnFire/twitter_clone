from django.db import models

from post_tweets.models.post import Post
from users.models.user import User

class FeedPost(models.Model):
    user = models.ForeignKey(User, related_name="post_tweet", on_delete=models.CASCADE)
    tweet = models.ForeignKey(Post, related_name="post_tweet", on_delete=models.CASCADE, null=True, blank=True,)
    content = models.CharField(max_length=254)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
from rest_framework import serializers

from login.models.login import Login
from post_tweets.models.post import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'updated_on',
            'content',
            'created_on',
            'status',
        ]
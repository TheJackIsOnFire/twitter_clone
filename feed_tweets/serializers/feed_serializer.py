from rest_framework import serializers
from feed_tweets.models.feed import FeedPost
from users.models.user import User
from users.serializers.user_serializer import UserSerializer

class FeedPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedPost
        fields = ('id', 'user', 'tweet', 'content', 'read', 'created_at')
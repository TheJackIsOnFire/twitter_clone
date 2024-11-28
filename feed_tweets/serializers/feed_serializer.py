from rest_framework import serializers

from feed_tweets.models.feed import FeedPost

class FeedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPost
        fields = ['id', 'user', 'tweet', 'content', 'read', 'created_at']
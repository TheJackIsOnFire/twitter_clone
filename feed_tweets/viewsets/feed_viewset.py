from rest_framework import viewsets

from feed_tweets.models.feed import FeedPost
from feed_tweets.serializers.feed_serializer import FeedPostSerializer


class FeedPostViewSet(viewsets.ModelViewSet):
    queryset = FeedPost.objects.all().order_by('created_at')
    serializer_class = FeedPostSerializer

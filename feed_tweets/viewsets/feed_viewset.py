from rest_framework import viewsets

from feed_tweets.serializers.feed_serializer import FeedPostSerializer
from post_tweets.models.post import Post


class FeedPostViewSet(viewsets.ModelViewSet):
    serializer_class = FeedPostSerializer

    def get_queryset(self):
        return Post.objects.all()
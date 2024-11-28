from rest_framework.viewsets import ModelViewSet

from post_tweets.models.post import Post
from post_tweets.serializers.post_serializer import PostSerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
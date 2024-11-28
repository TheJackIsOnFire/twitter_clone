from django.urls import path, include
from rest_framework import routers

from feed_tweets import viewsets

router = routers.SimpleRouter()
router.register(r'feed_tweets', viewsets.FeedPostViewSet, basename='feed_tweets')

urlpatterns = [
    path('', include(router.urls)),
]
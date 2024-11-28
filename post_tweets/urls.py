from django.urls import path, include
from rest_framework import routers

from post_tweets import viewsets

router = routers.SimpleRouter()
router.register(r'post_tweets', viewsets.PostViewSet, basename='post_tweets')

urlpatterns = [
    path('', include(router.urls)),
]
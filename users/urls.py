from django.urls import path, include
from rest_framework import routers

from users import viewsets

router = routers.SimpleRouter()
router.register(r'user', viewsets.UserViewSet, basename='user')
router.register(r'user_connections', viewsets.UserConnectionsViewSet, basename='user_connections')

urlpatterns = [
    path('', include(router.urls)),
]
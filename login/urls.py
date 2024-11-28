from django.urls import path, include
from rest_framework import routers

from login import viewsets

router = routers.SimpleRouter()
router.register(r'login', viewsets.LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework.viewsets import ModelViewSet

from login.models.login import Login
from login.serializers.login_serializer import LoginSerializer

class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer

    def get_queryset(self):
        return Login.objects.all()
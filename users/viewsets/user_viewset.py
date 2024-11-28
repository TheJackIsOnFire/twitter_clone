from rest_framework.viewsets import ModelViewSet

from users.models.user import User
from users.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('id')
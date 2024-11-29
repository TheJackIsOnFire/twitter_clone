from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from users.models.user import User
from users.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUser(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserSerializer    
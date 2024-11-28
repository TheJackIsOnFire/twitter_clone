from rest_framework import serializers

from users.models import UserConnections
from users.serializers.user_serializer import UserSerializer


class UserConnectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserConnections
        fields = ['user_main', 'followed','follower']
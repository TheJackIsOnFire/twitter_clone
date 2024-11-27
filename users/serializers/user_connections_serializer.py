from rest_framework import serializers

from users.models.user_connection import UserConnections


class UserConnectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserConnections
        fields = [
            'id',
            'main_user',
            'followed',
            'following',
        ]
from rest_framework.viewsets import ModelViewSet

from users.models.user_connections import UserConnections
from users.serializers.user_connections_serializer import UserConnectionsSerializer

class UserConnectionsViewSet(ModelViewSet):
    serializer_class = UserConnectionsSerializer

    def get_queryset(self):
        return UserConnections.objects.all()
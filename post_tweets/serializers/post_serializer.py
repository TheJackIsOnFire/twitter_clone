from rest_framework import serializers

from post_tweets.models.post import Post
from users.models.user import User

# Serializer para o modelo Post
class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'created_on', 'updated_on', 'status']
        read_only_fields = ['id', 'created_on', 'updated_on']  # Garantir que campos de data não sejam editados

    def validate_status(self, value):
        """Valida o campo de status para garantir que o valor esteja correto."""
        if value not in [0, 1]:
            raise serializers.ValidationError("Status inválido. Deve ser 0 (Draft) ou 1 (Publish).")
        return value

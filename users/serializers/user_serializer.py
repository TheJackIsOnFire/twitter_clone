from rest_framework import serializers
from users.models.user import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        #style={'input_type': 'password'},
        write_only=True,
        label="Password"
    )

    password_confirm = serializers.CharField(
        #style={'input_type': 'password'},
        write_only=True,
        label="Confirm password",
    )

    class Meta:
        model = User
        fields = (
            'id',
            'fullname',
            'username',
            'email',
            'password',
            'password_confirm',
            'created_at'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        
        return data

    def create(self, validated_data):
        # Remover o campo 'password_confirm' do validated_data antes de salvar
        validated_data.pop('password_confirm', None)

        # Criar o usuário sem o campo 'password_confirm'
        user = User(
            fullname=validated_data['fullname'],
            username=validated_data['username'],
            email=validated_data['email'],
        )
        # Configurar a senha e salvar o usuário
        #user.set_password(validated_data['password'])
        user.save()
        
        return user


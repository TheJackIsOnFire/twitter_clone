from rest_framework import serializers
from login.models import Login
from users.models.user import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        #style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        #style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    class Meta:
        model = Login
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Validação da senha e confirmação de senha
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        
        return data

    def create(self, validated_data):
        # Remover o campo 'password_confirm' antes de criar o Login ou User
        validated_data.pop('password_confirm', None)

        # Verificar se o usuário com o username e email fornecidos existe
        user = User.objects.filter(username=validated_data['username'], email=validated_data['email']).first()

        if not user:
            raise serializers.ValidationError({'username': 'Usuário não encontrado com esse nome de usuário e email.'})
        
        # Verificar se a senha está correta
        password = validated_data['password']
        if not password:
            raise serializers.ValidationError({'password': 'Senha incorreta.'})

        # Se o login for bem-sucedido, você pode retornar o objeto Login
        login = Login(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        
        # Criar o usuário relacionado, se necessário
        # user.set_password(validated_data['password']) # Não é necessário redefinir a senha para login
        # user.save()  # Não é necessário salvar o usuário novamente
        
        login.user = user  # Associar o usuário ao login
        login.save()

        return login

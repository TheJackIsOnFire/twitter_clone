from django.test import TestCase
from users.models import User, UserConnections

class UserConnectionsModelTest(TestCase):

    def setUp(self):
        """Cria usuários e conexões iniciais para os testes."""
        self.user_main = User.objects.create(
            fullname="Main User",
            username="@mainuser",
            email="main.user@example.com",
            password="mainpassword123"
        )
        self.follower = User.objects.create(
            fullname="Follower User",
            username="@followeruser",
            email="follower.user@example.com",
            password="followerpassword123"
        )
        self.followed = User.objects.create(
            fullname="Followed User",
            username="@followeduser",
            email="followed.user@example.com",
            password="followedpassword123"
        )

        self.connection = UserConnections.objects.create(
            user_main=self.user_main,
            follower=self.follower,
            followed=self.followed
        )

    def test_user_connections_creation(self):
        """Teste para verificar se a conexão foi criada corretamente."""
        connection = UserConnections.objects.get(id=self.connection.id)
        self.assertEqual(connection.user_main, self.user_main)
        self.assertEqual(connection.follower, self.follower)
        self.assertEqual(connection.followed, self.followed)


    def test_related_name(self):
        """Teste para verificar os nomes relacionados."""
        self.assertEqual(self.user_main.user_main_set.count(), 1)
        self.assertEqual(self.follower.follower_set.count(), 1)
        self.assertEqual(self.followed.followed_set.count(), 1)

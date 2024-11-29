from django.test import TestCase

from users.factories import UserFactory
from users.serializers.user_connections_serializer import UserConnectionsSerializer


class TestUserConnectionSerializer(TestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory(id=1, fullname='Alexsander Wallace', username='Jack', email='alexsander@gmail.com', password='123')
        self.user_2 = UserFactory(id=2, fullname='alex', username='Jackal', email='alex@gmail.com', password='123')
        self.user_3 = UserFactory(id=3, fullname='andrade', username='the old Jack', email='andrade@gmail.com', password='123')
        
        self.user_connections_serializer = UserConnectionsSerializer(user_main=self.user_1, followed=self.user_2, follower=self.user_3)

    def test_product_serializer(self):
        serializer_data = self.user_connections_serializer.data
        self.assertEqual(serializer_data['user_main'], self.user_1)
        self.assertEqual(serializer_data['followed'], self.user_2)
        self.assertEqual(serializer_data['follower'], self.user_3)

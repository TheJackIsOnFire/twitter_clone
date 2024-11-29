from django.test import TestCase

from users.factories import UserFactory
from users.serializers import UserSerializer


class TestUserSerializer(TestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory(id=1, fullname='Alexsander Wallace', username='Jack', email='alex@gmail.com', password='123')
        self.user_serializer = UserSerializer(self.user_1)

    def test_product_serializer(self):
        serializer_data = self.user_serializer.data
        self.assertEqual(serializer_data['id'], 1)
        self.assertEqual(serializer_data['fullname'], 'Alexsander Wallace')
        self.assertEqual(serializer_data['username'], 'Jack')
        self.assertEqual(serializer_data['email'], 'alex@gmail.com')
        self.assertEqual(serializer_data['password'], '123')

from django.test import TestCase

from users.models.user import User


class UserModelTest(TestCase):

    def setUp(self):
        """Cria um usuário inicial para os testes."""
        self.user = User.objects.create(
            fullname="John Doe",
            username="@johndoe",
            email="john.doe@example.com",
            password="securepassword123"
        )

    def test_user_creation(self):
        """Teste para verificar se o usuário foi criado corretamente."""
        user = User.objects.get(username="@johndoe")
        self.assertEqual(user.fullname, "John Doe")
        self.assertEqual(user.email, "john.doe@example.com")

    def test_username_unique_constraint(self):
        """Teste para verificar se o campo username é único."""
        with self.assertRaises(Exception):
            User.objects.create(
                fullname="Jane Doe",
                username="@johndoe",  # Mesmo username
                email="jane.doe@example.com",
                password="anotherpassword123"
            )

    def test_email_unique_constraint(self):
        """Teste para verificar se o campo email é único."""
        with self.assertRaises(Exception):
            User.objects.create(
                fullname="Jane Doe",
                username="@janedoe",
                email="john.doe@example.com",  # Mesmo email
                password="anotherpassword123"
            )

    def test_default_values(self):
        """Teste para verificar os valores padrão de username e email."""
        user = User.objects.create(
            fullname="Default User",
            password="defaultpassword123"
        )
        self.assertEqual(user.username, "@username")
        self.assertEqual(user.email, "xxx@email.com")

    def test_str_representation(self):
        """Teste para verificar o método __str__ do modelo."""
        self.assertEqual(str(self.user), "@johndoe")

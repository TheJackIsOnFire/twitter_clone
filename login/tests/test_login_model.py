from django.test import TestCase
from login.models import Login

class LoginModelTest(TestCase):

    def setUp(self):
        """Cria uma instância de Login para os testes."""
        self.login = Login.objects.create(
            username="testuser",
            email="testuser@example.com",
            password="securepassword123"
        )

    def test_login_creation(self):
        """Teste para verificar se o login foi criado corretamente."""
        login = Login.objects.get(username="testuser")
        self.assertEqual(login.email, "testuser@example.com")
        self.assertEqual(login.password, "securepassword123")

    def test_username_unique_constraint(self):
        """Teste para verificar se o campo username é único."""
        with self.assertRaises(Exception):
            Login.objects.create(
                username="testuser",  # Mesmo username
                email="anotheruser@example.com",
                password="anotherpassword123"
            )

    def test_email_unique_constraint(self):
        """Teste para verificar se o campo email é único."""
        with self.assertRaises(Exception):
            Login.objects.create(
                username="anotheruser",
                email="testuser@example.com",  # Mesmo email
                password="anotherpassword123"
            )

    def test_data_time_auto_now_add(self):
        """Teste para verificar se data_time é preenchido automaticamente."""
        self.assertIsNotNone(self.login.data_time)



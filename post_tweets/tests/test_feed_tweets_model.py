from django.test import TestCase
from users.models.user import User
from post_tweets.models import Post

class PostModelTest(TestCase):

    def setUp(self):
        """Cria um usuário e um post inicial para os testes."""
        self.user = User.objects.create(
            fullname="Author User",
            username="@authoruser",
            email="author.user@example.com",
            password="authorpassword123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="This is a test post content",
            status=1
        )

    def test_post_creation(self):
        """Teste para verificar se o post foi criado corretamente."""
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, "This is a test post content")
        self.assertEqual(post.status, 1)

    def test_post_default_status(self):
        """Teste para verificar se o status padrão é Draft (0)."""
        post = Post.objects.create(
            title="Draft Post",
            author=self.user,
            content="This is a draft post"
        )
        self.assertEqual(post.status, 0)

    def test_updated_on_auto_now(self):
        """Teste para verificar se updated_on é atualizado automaticamente."""
        old_updated_on = self.post.updated_on
        self.post.content = "Updated content"
        self.post.save()
        self.assertNotEqual(self.post.updated_on, old_updated_on)

    def test_created_on_auto_now_add(self):
        """Teste para verificar se created_on é preenchido automaticamente."""
        self.assertIsNotNone(self.post.created_on)

    def test_post_ordering(self):
        """Teste para verificar a ordenação dos posts por created_on."""
        post2 = Post.objects.create(
            title="Newer Post",
            author=self.user,
            content="This is a newer post",
            status=1
        )
        posts = Post.objects.all()
        self.assertEqual(posts[0], self.post)
        self.assertEqual(posts[1], post2)

    def test_str_representation(self):
        """Teste para verificar o método __str__ do modelo."""
        self.assertEqual(str(self.post), "Test Post")

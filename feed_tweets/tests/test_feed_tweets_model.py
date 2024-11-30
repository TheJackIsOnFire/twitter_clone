from django.test import TestCase
from post_tweets.models.post import Post
from users.models.user import User
from feed_tweets.models import FeedPost

class FeedPostModelTest(TestCase):

    def setUp(self):
        """Cria um usuário, um post e um feed inicial para os testes."""
        self.user = User.objects.create(
            fullname="Test User",
            username="@testuser",
            email="test.user@example.com",
            password="password123"
        )
        self.post = Post.objects.create(
            title="Test Tweet",
            author=self.user,
            content="This is a test tweet content",
            status=1
        )
        self.feed_post = FeedPost.objects.create(
            user=self.user,
            tweet=self.post,
            content="This is a feed content",
            read=False
        )

    def test_feedpost_creation(self):
        """Teste para verificar se o FeedPost foi criado corretamente."""
        feed_post = FeedPost.objects.get(id=self.feed_post.id)
        self.assertEqual(feed_post.user, self.user)
        self.assertEqual(feed_post.tweet, self.post)
        self.assertEqual(feed_post.content, "This is a feed content")
        self.assertFalse(feed_post.read)

    def test_default_read_status(self):
        """Teste para verificar se o status padrão de 'read' é False."""
        feed_post = FeedPost.objects.create(
            user=self.user,
            tweet=self.post,
            content="Another feed content"
        )
        self.assertFalse(feed_post.read)

    def test_created_at_auto_now_add(self):
        """Teste para verificar se created_at é preenchido automaticamente."""
        self.assertIsNotNone(self.feed_post.created_at)


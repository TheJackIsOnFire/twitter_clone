import factory

from .models.user import User
from .models.user_connections import UserConnections


class UserFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('pyint')
    fullname = factory.Faker('pystr')
    username = factory.Faker('pystr')
    email = factory.Faker('pystr')
    password = factory.Faker('pystr')

    class Meta:
        model = User


class UserConnectionsFactory(factory.django.DjangoModelFactory):
    user_main = factory.Faker('UserFactory')
    followed = factory.Faker('UserFactory')
    follower = factory.Faker('UserFactory')

    class Meta:
        model = UserConnections

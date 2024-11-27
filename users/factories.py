import factory

from .models.user import User
from .models.user_connection import UserConnections


class UserFactory(factory.django.DjangoModelFactory):
    fullname = factory.Faker('pystr')
    username = factory.Faker('pystr')
    email = factory.Faker('pystr')
    password = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = User


class ProductFactory(factory.django.DjangoModelFactory):
    main_user = factory.Faker('pystr')
    followed = factory.Faker('pystr')
    following = factory.Faker('pystr')

    class Meta:
        model = UserConnections

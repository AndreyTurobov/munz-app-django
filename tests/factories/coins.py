import factory
from factory.django import DjangoModelFactory

from core.apps.coins.models.coins import Coin


class CoinModelFactory(DjangoModelFactory):
    title = factory.Faker('first_name')
    country = factory.Faker('country')
    issue_at = factory.Faker('date_of_birth')

    class Meta:
        model = Coin

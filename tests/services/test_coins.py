"""
1. Test coins count: coin count zero, coin count with existing coins
2. Test coin returns all, with paginagion, test filters (title, country, issue_at, no match)
"""

import pytest
from tests.factories.coins import CoinModelFactory

from core.api.filters import PaginationIn
from core.api.v1.coins.filters import CoinFilters
from core.apps.coins.services.coins import BaseCoinService


@pytest.mark.django_db
def test_get_coins_count_zero(coin_service: BaseCoinService):
    """Test coin count zero with no coins in database."""
    coins_count = coin_service.get_coin_count(CoinFilters())
    assert coins_count == 0, f'{coins_count=} '


@pytest.mark.django_db
def test_get_coins_count_exist(coin_service: BaseCoinService):
    """Test coin count with existing."""
    expected_count = 5
    CoinModelFactory.create_batch(size=expected_count)

    coins_count = coin_service.get_coin_count(CoinFilters())
    assert coins_count == expected_count, f'{coins_count=} '


@pytest.mark.django_db
def test_get_coins_all(coin_service: BaseCoinService):
    """Test all coins retrieved from database."""
    expected_count = 5
    coins = CoinModelFactory.create_batch(size=expected_count)
    coins_titles = {coin.title for coin in coins}

    fetched_coins = coin_service.get_coin_list(CoinFilters(), PaginationIn())
    fetched_titles = {coin.title for coin in fetched_coins}

    assert len(fetched_titles) == expected_count, f'{fetched_titles=} '
    assert coins_titles == fetched_titles, f'{coins_titles} '

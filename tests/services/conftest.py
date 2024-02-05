import pytest

from core.apps.coins.services.coins import (
    BaseCoinService,
    ORMCoinService,
)


@pytest.fixture
def coin_service() -> BaseCoinService:
    return ORMCoinService()

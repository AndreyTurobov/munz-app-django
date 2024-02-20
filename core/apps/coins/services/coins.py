from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.api.v1.coins.filters import CoinFilters
from core.api.v1.coins.schemas import CoinSchemaIn
from core.apps.coins.entities.coins import Coin
from core.apps.coins.models.coins import Coin as CoinModel


class BaseCoinService(ABC):
    @abstractmethod
    def create_coin(
        self,
        schema: CoinSchemaIn,
    ) -> Coin: ...

    @abstractmethod
    def get_coin_list(
        self,
        filters: CoinFilters,
        pagination: PaginationIn,
    ) -> Iterable[Coin]: ...

    @abstractmethod
    def get_coin_count(
        self,
        filters: CoinFilters,
    ) -> int: ...


# TODO: закинуть фильтры в сервисный слой,чтобы избежать нарушения D из SOLID
class ORMCoinService(BaseCoinService):
    def create_coin(
        self,
        schema: CoinSchemaIn,
    ) -> Coin:
        coin = CoinModel.objects.create(**schema.dict(exclude_unset=True))
        return coin.to_entity()

    def _build_coin_query(
        self,
        filters: CoinFilters,
    ) -> Q:
        query = Q(title__startswith="")

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )

        return query

    def get_coin_list(
        self,
        filters: CoinFilters,
        pagination: PaginationIn,
    ) -> Iterable[Coin]:
        query = self._build_coin_query(filters)
        qs = CoinModel.objects.filter(query)[
            pagination.offset : pagination.offset + pagination.limit
        ]

        return [coin.to_entity() for coin in qs]

    def get_coin_count(self, filters: CoinFilters) -> int:
        query = self._build_coin_query(filters)

        return CoinModel.objects.filter(query).count()

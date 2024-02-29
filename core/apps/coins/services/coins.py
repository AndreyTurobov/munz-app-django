from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q
from django.shortcuts import get_object_or_404

from core.api.filters import PaginationIn
from core.api.v1.coins.schemas import (
    CoinSchemaIn,
    PatchCoinSchemaIn,
)
from core.apps.coins.entities.coins import Coin
from core.apps.coins.filters.coins import CoinFilters
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

    @abstractmethod
    def update_coin(
        self,
        coin_id: int,
        schema: CoinSchemaIn,
    ) -> Coin: ...

    @abstractmethod
    def partial_update_coin(
        self,
        coin_id: int,
        schema: PatchCoinSchemaIn,
    ) -> Coin: ...

    @abstractmethod
    def delete_coin(
        self,
        coin_id: int,
    ) -> None: ...


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

    def update_coin(
        self,
        coin_id: int,
        schema: CoinSchemaIn,
    ) -> Coin:
        coin = get_object_or_404(CoinModel, id=coin_id)
        for attr, value in schema.dict(exclude_unset=True).items():
            setattr(coin, attr, value)
        coin.save()
        return coin

    def partial_update_coin(
        self,
        coin_id: int,
        schema: PatchCoinSchemaIn,
    ) -> Coin:
        coin = get_object_or_404(CoinModel, id=coin_id)
        for attr, value in schema.dict(exclude_unset=True).items():
            setattr(coin, attr, value)
        coin.save()
        return coin

    def delete_coin(
        self,
        coin_id: int,
    ) -> None:
        coin = get_object_or_404(CoinModel, id=coin_id)
        coin.delete()
        return {'success': True}

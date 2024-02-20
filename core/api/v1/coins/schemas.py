from datetime import datetime
from typing import Optional

from ninja import Schema

from core.apps.coins.entities.coins import Coin as CoinEntity


class CoinSchemaIn(Schema):
    title: str
    description: str
    country: str
    issue_at: str
    state: str


class PatchCoinSchemaIn(Schema):
    description: Optional[str] = None
    issue_at: Optional[str] = None
    state: Optional[str] = None


class CoinSchemaOut(Schema):
    id: int  # noqa
    title: str
    description: str
    country: str
    issue_at: str
    state: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: CoinEntity) -> 'CoinSchemaOut':
        return CoinSchemaOut(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            country=entity.country,
            issue_at=entity.issue_at,
            state=entity.state,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


CoinListSchema = list[CoinSchemaOut]

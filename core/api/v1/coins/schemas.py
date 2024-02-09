from datetime import datetime

from pydantic import BaseModel

from core.apps.coins.entities.coins import Coin as CoinEntity


class CoinSchema(BaseModel):
    id: int  # noqa
    title: str
    description: str
    country: str
    issue_at: str
    state: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: CoinEntity) -> 'CoinSchema':
        return CoinSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            country=entity.country,
            issue_at=entity.issue_at,
            state=entity.state,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


CoinListSchema = list[CoinSchema]

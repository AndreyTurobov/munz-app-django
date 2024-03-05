from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from core.apps.coins.entities.coins import Coin
from core.apps.common.enums import EntityStatus
from core.apps.guests.entities import Guest


@dataclass
class Review:
    id: int | None = field(default=None, kw_only=True)  # noqa
    guest: Guest | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
    rating: int = field(default=1)
    coin: Coin | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    create_at: datetime = field(default_factory=datetime.utcnow)
    update_at: datetime | None = field(default=None)

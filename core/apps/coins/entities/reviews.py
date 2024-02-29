from dataclasses import (
    dataclass,
    field,
)

from core.apps.coins.entities.coins import Coin
from core.apps.common.enums import EntityStatus
from core.apps.guests.entities import Guest


@dataclass
class Review:
    guest: Guest | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
    rating: int = field(default=1)
    coin: Coin | EntityStatus = field(default=EntityStatus.NOT_LOADED)

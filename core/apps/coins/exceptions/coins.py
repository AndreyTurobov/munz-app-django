from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CoinNotFound(ServiceException):
    coin_id: int

    @property
    def message(self):
        return 'Coin not found'

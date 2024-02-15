from abc import (
    ABC,
    abstractmethod,
)

from core.apps.guests.entities import GuestEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, guest: GuestEntity, code: str) -> None: ...


class SenderService(BaseSenderService):
    def send_code(self, guest: GuestEntity, code: str) -> None:
        print(f'Code to guest: {guest} sent: {code}')

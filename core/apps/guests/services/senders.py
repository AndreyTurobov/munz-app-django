from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from core.apps.guests.entities import GuestEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, guest: GuestEntity, code: str) -> None: ...


class EmailSenderService(BaseSenderService):
    def send_code(self, guest: GuestEntity, code: str) -> None:
        print(f'Sent code {code} to guest email: guest_email')


class PushSenderService(BaseSenderService):
    def send_code(self, guest: GuestEntity, code: str) -> None:
        print(f'Sent code {code} as push notification: fcm_token')


@dataclass
class ComposedSenderService(BaseSenderService):
    sender_services: Iterable[BaseSenderService]

    def send_code(self, guest: GuestEntity, code: str) -> None:
        for service in self.sender_services:
            service.send_code(guest, code)

from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.guests.entities import Guest
from core.apps.guests.models import Guest as GuestModel


class BaseGuestService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> Guest: ...

    @abstractmethod
    def generate_token(self, guest: Guest) -> str: ...

    @abstractmethod
    def get(self, phone: str) -> Guest: ...


class ORMGuestService(BaseGuestService):
    def get_or_create(self, phone: str) -> Guest:
        guest_dto, _ = GuestModel.objects.get_or_create(phone=phone)
        return guest_dto.to_entity()

    def get(self, phone: str) -> Guest:
        guest_dto = GuestModel.objects.get(phone=phone)
        return guest_dto.to_entity()

    def generate_token(self, guest: Guest) -> str:
        new_token = str(uuid4())
        GuestModel.objects.filter(phone=guest.phone).update(token=new_token)

        return new_token

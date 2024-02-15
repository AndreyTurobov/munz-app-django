from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.guests.entities import GuestEntity
from core.apps.guests.models import Guest as GuestModel


class BaseGuestService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> GuestEntity: ...

    @abstractmethod
    def generate_token(self, guest: GuestEntity) -> str: ...

    @abstractmethod
    def get(self, phone: str) -> GuestEntity: ...


class ORMGuestService(BaseGuestService):
    def get_or_create(self, phone: str) -> GuestEntity:
        guest_dto, _ = GuestModel.objects.get_or_create(phone=phone)
        return guest_dto.to_entity()

    def get(self, phone: str) -> GuestEntity:
        guest_dto = GuestModel.objects.get(phone=phone)
        return guest_dto.to_entity()

    def generate_token(self, guest: GuestEntity) -> str:
        new_token = str(uuid4())
        GuestModel.objects.filter(phone=guest.phone).update(token=new_token)

        return new_token

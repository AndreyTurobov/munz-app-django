from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.guests.services.codes import BaseCodeService
from core.apps.guests.services.guests import BaseGuestService
from core.apps.guests.services.senders import BaseSenderService


# TODO Remove business-logic and move in use-cases
@dataclass(eq=False)
class BaseAuthService(ABC):
    guest_service: BaseGuestService
    codes_service: BaseCodeService
    sender_service: BaseSenderService

    @abstractmethod
    def authorize(self, phone: str): ...

    @abstractmethod
    def confirm(self, code: str, phone: str): ...


class AuthService(BaseAuthService):
    def authorize(self, phone: str):
        guest = self.guest_service.get_or_create(phone)
        code = self.codes_service.generate_code(guest)
        self.sender_service.send_code(guest, code)

    def confirm(self, code: str, phone: str):
        guest = self.guest_service.get(phone)
        self.codes_service.validate_code(code, guest)
        return self.guest_service.generate_token(guest)

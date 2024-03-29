import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from core.apps.guests.entities import Guest
from core.apps.guests.exceptions.codes import (
    CodeNotFoundException,
    CodesNotEqualException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, guest: Guest) -> str: ...

    @abstractmethod
    def validate_code(self, code: str, guest: Guest) -> None: ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, guest: Guest) -> str:
        code = str(random.randint(100000, 999999))  # noqa
        cache.set(guest.phone, code)
        return code

    def validate_code(self, code: str, guest: Guest) -> None:
        cached_code = cache.get(guest.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if cached_code != code:
            raise CodesNotEqualException(
                code=code,
                cached_code=cached_code,
                guest_phone=guest.phone,
            )

        cache.delete(guest.phone)

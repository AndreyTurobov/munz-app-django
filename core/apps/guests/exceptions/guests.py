from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class GuestTokenInvalid(ServiceException):
    token: str

    @property
    def message(self):
        return 'Guest with provided token not found'

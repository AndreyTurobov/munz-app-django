from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.guests.schemas import (
    AuthInSchema,
    AuthOutSchema,
    TokenInSchema,
    TokenOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.guests.services.auth import AuthService
from core.apps.guests.services.codes import DjangoCacheCodeService
from core.apps.guests.services.guests import ORMGuestService
from core.apps.guests.services.senders import SenderService


router = Router(tags=['Guests'])


@router.post('auth', response=ApiResponse[AuthOutSchema], operation_id='authorize')
def auth_handler(
    request: HttpRequest,
    schema: AuthInSchema,
) -> ApiResponse[AuthOutSchema]:
    service = AuthService(
        guest_service=ORMGuestService(),
        codes_service=DjangoCacheCodeService(),
        sender_service=SenderService(),
    )
    service.authorize(schema.phone)
    return ApiResponse(
        data=AuthOutSchema(
            message=f'Code is sent to: {schema.phone}',
        ),
    )


@router.post(
    'confirm',
    response=ApiResponse[TokenOutSchema],
    operation_id='confirmCode',
)
def get_token_handler(
    request: HttpRequest,
    schema: TokenInSchema,
) -> ApiResponse[TokenOutSchema]:
    service = AuthService(
        guest_service=ORMGuestService(),
        codes_service=DjangoCacheCodeService(),
        sender_service=SenderService(),
    )
    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message,
        ) from exception

    return ApiResponse(data=TokenOutSchema(token=token))
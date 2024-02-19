from django.http import HttpRequest
from ninja import (
    Query,
    Router,
)

from core.api.filters import PaginationIn
from core.api.schemas import (
    ApiResponse,
    ListPaginatedResponse,
    PaginationOut,
)
from core.api.v1.coins.filters import CoinFilters
from core.api.v1.coins.schemas import CoinSchema
from core.apps.coins.containers import get_container
from core.apps.coins.services.coins import BaseCoinService


router = Router(tags=['Coins'])


@router.get('', response=ApiResponse[ListPaginatedResponse[CoinSchema]])
def get_coin_list_handler(
    request: HttpRequest,
    filters: Query[CoinFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[CoinSchema]]:
    container = get_container()
    service: BaseCoinService = container.resolve(BaseCoinService)
    coin_list = service.get_coin_list(filters=filters, pagination=pagination_in)
    coin_count = service.get_coin_count(filters=filters)
    items = [CoinSchema.from_entity(obj) for obj in coin_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=coin_count,
    )

    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out),
    )

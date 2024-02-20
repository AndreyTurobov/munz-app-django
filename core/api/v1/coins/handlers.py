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
from core.api.v1.coins.schemas import (
    CoinSchemaIn,
    CoinSchemaOut,
    PatchCoinSchemaIn,
)
from core.apps.coins.containers import get_container
from core.apps.coins.services.coins import BaseCoinService


router = Router(tags=['Coins'])


@router.post('', response=ApiResponse[CoinSchemaOut])
def create_coin_handler(
    request: HttpRequest,
    schema: CoinSchemaIn,
) -> ApiResponse[CoinSchemaOut]:
    container = get_container()
    service: BaseCoinService = container.resolve(BaseCoinService)

    return ApiResponse(data=service.create_coin(schema=schema))


@router.get('', response=ApiResponse[ListPaginatedResponse[CoinSchemaOut]])
def get_coin_list_handler(
    request: HttpRequest,
    filters: Query[CoinFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[CoinSchemaOut]]:
    container = get_container()
    service: BaseCoinService = container.resolve(BaseCoinService)
    coin_list = service.get_coin_list(filters=filters, pagination=pagination_in)
    coin_count = service.get_coin_count(filters=filters)
    items = [CoinSchemaOut.from_entity(obj) for obj in coin_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=coin_count,
    )

    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out),
    )


@router.put('{coin_id}', response=ApiResponse[CoinSchemaIn])
def update_coin(
    request: HttpRequest,
    coin_id: int,
    schema: CoinSchemaIn,
) -> ApiResponse[CoinSchemaOut]:
    container = get_container()
    service: BaseCoinService = container.resolve(BaseCoinService)
    return ApiResponse(data=service.update_coin(coin_id=coin_id, schema=schema))


@router.patch('{coin_id}', response=ApiResponse[PatchCoinSchemaIn])
def partial_update_coin(
    request: HttpRequest,
    coin_id: int,
    schema: PatchCoinSchemaIn,
) -> ApiResponse[CoinSchemaOut]:
    container = get_container()
    service: BaseCoinService = container.resolve(BaseCoinService)
    return ApiResponse(data=service.partial_update_coin(coin_id=coin_id, schema=schema))


@router.delete('{coin_id}')
def delete_coin(request: HttpRequest, coin_id: int) -> None:
    container = get_container()
    service: BaseCoinService = container.resolve(BaseCoinService)
    return service.delete_coin(coin_id=coin_id)

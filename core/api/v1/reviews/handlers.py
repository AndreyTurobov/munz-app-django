from logging import Logger

from django.http import HttpRequest
from ninja import (
    Header,
    Router,
)
from ninja.errors import HttpError

import orjson

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import (
    ReviewInSchema,
    ReviewOutSchema,
)
from core.apps.coins.use_cases.reviews.create import CreateReviewUseCase
from core.apps.common.exceptions import ServiceException
from core.project.containers import get_container


router = Router(tags=['Reviews'])


@router.post(
    '{coin_id}/reviews',
    response=ApiResponse[ReviewOutSchema],
    operation_id='createReview',
)
def create_review(
    request: HttpRequest,
    coin_id: int,
    schema: ReviewInSchema,
    token: str = Header(alias='Auth-Token'),
) -> ApiResponse[ReviewOutSchema]:
    raise Exception(123)
    container = get_container()
    use_case: CreateReviewUseCase = container.resolve(CreateReviewUseCase)

    try:
        result = use_case.execute(
            guest_token=token,
            coin_id=coin_id,
            review=schema.to_entity(),
        )
    except ServiceException as error:
        logger: Logger = container.resolve(Logger)
        logger.error(
            msg='User could not create review',
            extra={'error_meta': orjson.dumps(error).decode()},
        )
        raise HttpError(
            status_code=400,
            message=error.message,
        ) from error

    return ApiResponse(data=ReviewOutSchema.from_entity(result))

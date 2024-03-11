from dataclasses import dataclass
from logging import Logger

from core.apps.coins.entities.reviews import Review as ReviewEntity
from core.apps.coins.services.coins import BaseCoinService
from core.apps.coins.services.reviews import (
    BaseReviewService,
    BaseReviewValidatorService,
)
from core.apps.guests.services.guests import BaseGuestService


@dataclass
class CreateReviewUseCase:
    coin_service: BaseCoinService
    review_service: BaseReviewService
    validator_service: BaseReviewValidatorService
    guest_service: BaseGuestService
    logger: Logger

    def execute(
        self,
        coin_id: int,
        review: ReviewEntity,
        guest_token: str,
    ) -> ReviewEntity:
        guest = self.guest_service.get_by_token(token=guest_token)
        coin = self.coin_service.get_by_id(coin_id=coin_id)
        self.validator_service.validate(
            review=review,
            guest=guest,
            coin=coin,
        )
        saved_review = self.review_service.save_review(
            review=review,
            guest=guest,
            coin=coin,
        )

        return saved_review

from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.coins.entities.coins import Coin as CoinEntity
from core.apps.coins.entities.reviews import Review as ReviewEntity
from core.apps.coins.exceptions.reviews import ReviewInvalidRating
from core.apps.coins.models.reviews import Review as ReviewModel
from core.apps.guests.entities import Guest as GuestEntity


class BaseReviewService(ABC):
    @abstractmethod
    def save_review(
        self,
        review: ReviewEntity,
        guest: GuestEntity,
        coin: CoinEntity,
    ) -> ReviewEntity: ...


class ORMReviewService(BaseReviewService):
    def save_review(
        self,
        review: ReviewEntity,
        guest: GuestEntity,
        coin: CoinEntity,
    ) -> ReviewEntity:
        review_dto: ReviewModel = ReviewModel.from_entity(
            review=review,
            guest=guest,
            coin=coin,
        )
        review_dto.save()

        return review_dto.to_entity()


class BaseReviewValidatorService(ABC):
    def validate(
        self,
        review: ReviewEntity,
        guest: GuestEntity | None = None,
        coin: CoinEntity | None = None,
    ): ...


class ReviewRatingValidatorService(BaseReviewValidatorService):
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ):
        # TODO: Add constants
        if not (1 <= review.rating <= 5):
            raise ReviewInvalidRating(rating=review.rating)


@dataclass
class ComposedReviewValidatorService(BaseReviewValidatorService):
    validators: list[BaseReviewValidatorService]

    def validate(
        self,
        review: ReviewEntity,
        guest: GuestEntity | None = None,
        coin: CoinEntity | None = None,
    ):
        for validator in self.validators:
            validator.validate(
                review=review,
                guest=guest,
                coin=coin,
            )

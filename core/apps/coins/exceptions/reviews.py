from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class ReviewInvalidRating(ServiceException):
    rating: int

    @property
    def message(self):
        return 'Rating is not valid'


@dataclass(eq=False)
class SingleReviewError(ServiceException):
    coin_id: int
    guest_id: int

    @property
    def message(self):
        return 'User already posted review on this product'

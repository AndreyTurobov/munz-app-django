from datetime import datetime

from pydantic import BaseModel

from core.apps.coins.entities.reviews import Review as ReviewEntity


class ReviewInSchema(BaseModel):
    rating: int
    text: str

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            rating=self.rating,
            text=self.text,
        )


class CreateReviewSchema(BaseModel):
    coin_id: int
    guest_token: str
    review: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int  # noqa
    create_at: datetime
    update_at: datetime | None

    @classmethod
    def from_entity(cls, review: ReviewEntity) -> 'ReviewOutSchema':
        return cls(
            id=review.id,
            rating=review.rating,
            text=review.text,
            create_at=review.create_at,
            update_at=review.update_at,
        )

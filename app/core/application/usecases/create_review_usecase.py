from typing import Optional
from uuid import UUID
from app.core.domain.entities.review_entity import ReviewEntity
from app.core.domain.ports.review_ports import ReviewRepositoryPort


class CreateReviewUseCase:
    """
    Use case for creating a review.
    """

    def __init__(self, repository: ReviewRepositoryPort):
        """
        Initializes the use case with the provided review repository.
        """
        self.repository = repository

    async def execute(self, recommendation: str, cat_uuid: UUID, loc_uuid: UUID,
                      obs: Optional[str] = "") -> ReviewEntity:
        """
        Creates a new review and saves it to the database.
        """
        # Create the review entity using provided information
        reviewed = ReviewEntity.create(
            recommendation=recommendation,
            loc_uuid=loc_uuid,  # Location UUID
            cat_uuid=cat_uuid,  # Category UUID
            obs=obs
        )

        # Save the review entity to the database
        await self.repository.save(reviewed)
        return reviewed


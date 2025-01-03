from app.adapters.secondary.orm.models import ModelReview
from app.core.domain.ports.review_ports import ReviewRepositoryPort

class ReviewRepository(ReviewRepositoryPort):
    """
    Repository for managing reviews in the system.
    This repository interacts with the database to save reviews.
    """

    async def save(self, review):
        """
        Save a new review to the database.
        The method assumes that the UUIDs for location and category are already correctly set.
        This method maps the entities to the corresponding database fields and stores the review.
        """

        # Save the review to the ModelReview table in the database
        await ModelReview.create(
            rev_uuid=review.rev_uuid,  # Unique identifier for the review
            rev_recommendation=review.rev_recommendation,  # The recommendation content of the review
            rev_obs=review.rev_obs,  # Optional observations for the review
            rev_created=review.rev_created,  # Timestamp when the review was created
            rev_fk_loc_uuid_id=review.rev_fk_loc_uuid,  # Foreign key to the Location entity (UUID)
            rev_fk_cat_uuid_id=review.rev_fk_cat_uuid,  # Foreign key to the Category entity (UUID)
        )



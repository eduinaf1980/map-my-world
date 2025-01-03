import uuid
from datetime import datetime
from typing import Optional
from uuid import UUID

class ReviewEntity:
    """
    Represents a review entity which includes a recommendation, an associated location and category,
    along with the creation date and optional observations.
    """

    def __init__(self, rev_uuid: UUID, rev_recommendation: str, rev_created: datetime, rev_fk_loc_uuid: UUID, rev_fk_cat_uuid: UUID, rev_obs: Optional[str] = None):
        """
        Initializes a ReviewEntity instance.

        :param rev_uuid: Unique identifier for the review.
        :param rev_recommendation: The actual recommendation made in the review.
        :param rev_created: The date and time when the review was created.
        :param rev_fk_loc_uuid: The UUID of the related location for this review.
        :param rev_fk_cat_uuid: The UUID of the related category for this review.
        :param rev_obs: Optional observations related to the review.
        """
        self.rev_uuid = rev_uuid
        self.rev_recommendation = rev_recommendation
        self.rev_obs = rev_obs
        self.rev_created = rev_created
        self.rev_fk_loc_uuid = rev_fk_loc_uuid
        self.rev_fk_cat_uuid = rev_fk_cat_uuid

    @staticmethod
    def create(recommendation: str, loc_uuid: UUID, cat_uuid: UUID, obs: Optional[str] = None) -> "ReviewEntity":
        """
        Factory method to create a new ReviewEntity instance.

        :param recommendation: The recommendation made in the review.
        :param loc_uuid: UUID of the location associated with the review.
        :param cat_uuid: UUID of the category associated with the review.
        :param obs: Optional observations related to the review.
        :return: A new instance of ReviewEntity.
        """
        return ReviewEntity(
            rev_uuid=uuid.uuid4(),  # Generate a new UUID for the review
            rev_recommendation=recommendation,
            rev_obs=obs,
            rev_created=datetime.utcnow(),  # Get the current UTC date and time
            rev_fk_loc_uuid=loc_uuid,  # Associate the location with the review
            rev_fk_cat_uuid=cat_uuid  # Associate the category with the review
        )

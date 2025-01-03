from uuid import UUID
from datetime import datetime
from typing import Optional


class RecommendationEntity:
    """
    Represents a recommendation entity consisting of a location and a category,
    along with a flag indicating whether it's reviewed or needs to be recommended,
    and the date of the review (if available).
    """

    def __init__(self, loc_uuid: UUID, loc_description: str, cat_uuid: UUID, cat_description: str, bandera: int,
                 review_date: Optional[datetime]):
        """
        Initializes a RecommendationEntity instance.

        :param loc_uuid: Unique identifier for the location.
        :param loc_description: Description of the location.
        :param cat_uuid: Unique identifier for the category.
        :param cat_description: Description of the category.
        :param bandera: Flag indicating the recommendation status:
                        1 = not reviewed, 2 = reviewed but old, 0 = recently reviewed.
        :param review_date: The date when the review was created, or None if not available.
        """
        self.loc_uuid = loc_uuid
        self.loc_description = loc_description
        self.cat_uuid = cat_uuid
        self.cat_description = cat_description
        self.bandera = bandera
        self.review_date = review_date

    def dict(self):
        """
        Serializes the RecommendationEntity object to a dictionary.

        :return: A dictionary representation of the RecommendationEntity instance.
        """
        return {
            "loc_uuid": str(self.loc_uuid),  # Convert UUID to string for JSON compatibility
            "loc_description": self.loc_description,
            "cat_uuid": str(self.cat_uuid),  # Convert UUID to string for JSON compatibility
            "cat_description": self.cat_description,
            "bandera": self.bandera,
            "review_date": self.review_date.isoformat() if self.review_date else None
            # Convert datetime to string (ISO format) or None
        }

    @staticmethod
    def create(loc_uuid: UUID, loc_description: str, cat_uuid: UUID, cat_description: str, bandera: int,
               review_date: Optional[datetime]) -> "RecommendationEntity":
        """
        Factory method to create a new RecommendationEntity instance.

        :param loc_uuid: Unique identifier for the location.
        :param loc_description: Description of the location.
        :param cat_uuid: Unique identifier for the category.
        :param cat_description: Description of the category.
        :param bandera: Flag indicating the recommendation status (1 = not reviewed, 2 = reviewed but old, 0 = recently reviewed).
        :param review_date: The date when the review was created or None if not available.
        :return: A new RecommendationEntity instance.
        """
        return RecommendationEntity(
            loc_uuid=loc_uuid,
            loc_description=loc_description,
            cat_uuid=cat_uuid,
            cat_description=cat_description,
            bandera=bandera,
            review_date=review_date
        )

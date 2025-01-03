from app.adapters.secondary.orm.models import ModelLocation, ModelCategory, ModelReview
from app.core.domain.ports.recommendation_ports import RecommendationRepositoryPort
from app.core.domain.entities.recomendation_entity import RecommendationEntity
from typing import List
from tortoise.exceptions import DoesNotExist
from datetime import datetime, timedelta
import pytz

class RecommendationRepository(RecommendationRepositoryPort):
    """
    Repository for handling recommendations.
    Retrieves and creates recommendations based on location and category combinations.
    """

    async def get_recommendations(self) -> List[RecommendationEntity]:
        """
        Retrieves up to 10 recommendations based on location-category combinations.
        Prioritizes combinations that haven't been reviewed in the last 30 days.
        """

        # Retrieve all locations and categories from the database
        all_locations = await ModelLocation.all()
        all_categories = await ModelCategory.all()

        recommendations = []

        # Get current time in UTC
        datetime_now_aware = datetime.now(pytz.UTC)

        # Iterate over all combinations of location and category
        for location in all_locations:
            for category in all_categories:
                try:
                    # Try to get the latest review for this location-category combination
                    last_review = await ModelReview.filter(
                        rev_fk_loc_uuid=location.loc_uuid,
                        rev_fk_cat_uuid=category.cat_uuid,
                        rev_created__lt=datetime_now_aware - timedelta(days=30)
                    ).order_by('-rev_created').first()  # Get the most recent review

                    # Check if the review exists
                    if last_review is None:
                        bandera = 1  # No review found
                        review_date = None
                    elif last_review.rev_created < datetime_now_aware - timedelta(days=30):
                        bandera = 2  # Review is older than 30 days
                        review_date = last_review.rev_created
                    else:
                        bandera = 0  # Review is recent
                        review_date = last_review.rev_created

                    # Create recommendation with the flag and review date
                    recommendations.append(RecommendationEntity(
                        loc_uuid=location.loc_uuid,
                        loc_description=location.loc_description,
                        cat_uuid=category.cat_uuid,
                        cat_description=category.cat_description,
                        bandera=bandera,
                        review_date=review_date
                    ))

                except DoesNotExist:
                    # If no review exists for this combination, assign flag 1
                    recommendations.append(RecommendationEntity(
                        loc_uuid=location.loc_uuid,
                        loc_description=location.loc_description,
                        cat_uuid=category.cat_uuid,
                        cat_description=category.cat_description,
                        bandera=1,
                        review_date=None
                    ))

        # Return only the top 10 recommendations
        return recommendations[:10]  # We return only the first 10 recommendations

from typing import List
from app.core.domain.entities.recomendation_entity import RecommendationEntity


class RecommendationRepositoryPort():
    """
    Abstract base class for the Recommendation repository port.
    Defines the method to fetch recommendations.
    """

    async def get_recommendations(self) -> List[RecommendationEntity]:
        """
        Fetch recommendations from the data source.

        :return: A list of RecommendationEntity objects.
        :raises NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError

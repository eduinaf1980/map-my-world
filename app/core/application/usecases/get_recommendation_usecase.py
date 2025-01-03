from app.core.domain.ports.recommendation_ports import RecommendationRepositoryPort
from app.core.domain.entities.recomendation_entity import RecommendationEntity
from typing import List

class GetRecommendationsUseCase:
    """
    Use case for retrieving recommendations.
    """

    def __init__(self, repository: RecommendationRepositoryPort):
        """
        Initializes the use case with the provided recommendation repository.
        """
        self.repository = repository

    async def execute(self) -> List[RecommendationEntity]:
        """
        Executes the use case to retrieve recommendations from the repository.
        """
        return await self.repository.get_recommendations()



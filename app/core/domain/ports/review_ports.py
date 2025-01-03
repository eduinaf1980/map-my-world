from abc import ABC, abstractmethod
from app.core.domain.entities.review_entity import ReviewEntity

class ReviewRepositoryPort(ABC):
    """
    Abstract base class for the Review repository port.
    Defines the method to save a review entity.
    """

    @abstractmethod
    async def save(self, review: ReviewEntity) -> None:
        """
        Save the provided review entity to the data source.

        :param review: The ReviewEntity object to be saved.
        :raises NotImplementedError: This method must be implemented in a subclass.
        """
        pass

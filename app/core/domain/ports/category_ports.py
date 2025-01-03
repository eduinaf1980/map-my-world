from abc import ABC, abstractmethod
from typing import Optional

from app.core.domain.entities.category_entity import CategoryEntity


class CategoryRepositoryPort(ABC):
    """
    Abstract base class for the Category repository port, defining the methods
    that should be implemented for interacting with category data.
    """

    @abstractmethod
    async def save(self, category: CategoryEntity) -> None:
        """
        Save a category entity.

        :param category: The category entity to be saved.
        """
        pass

    @abstractmethod
    async def get_by_description(self, description: str) -> Optional[CategoryEntity]:
        """
        Retrieve a category by its description.

        :param description: The description of the category to be fetched.
        :return: An optional CategoryEntity if found, otherwise None.
        """
        pass


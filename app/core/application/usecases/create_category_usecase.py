from app.core.domain.entities.category_entity import CategoryEntity
from app.core.domain.ports.category_ports import CategoryRepositoryPort
from app.core.domain.exceptions.exceptions import DuplicateCategoryError

class CreateCategoryUseCase:
    """
    Use case for creating a new category.
    """

    def __init__(self, repository: CategoryRepositoryPort):
        """
        Initializes the use case with the provided category repository.

        Args:
            repository: Category repository for fetching and saving data.
        """
        self.repository = repository

    async def execute(self, description: str) -> CategoryEntity:
        """
        Creates a new category if one doesn't already exist with the given description.

        Args:
            description: Category description to be created.

        Returns:
            CategoryEntity: The created category.

        Raises:
            DuplicateCategoryError: If a category with the same description exists.
        """
        # Check if the category already exists
        existing_category = await self.repository.get_by_description(description)
        if existing_category:
            raise DuplicateCategoryError("A category with this description already exists.")

        # Create and save the new category
        category = CategoryEntity.create(description)
        await self.repository.save(category)

        return category

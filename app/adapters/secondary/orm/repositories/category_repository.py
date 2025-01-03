from typing import Optional
from app.core.domain.entities.category_entity import CategoryEntity
from app.core.domain.ports.category_ports import CategoryRepositoryPort
from app.adapters.secondary.orm.models.category_model import ModelCategory
from tortoise.exceptions import DoesNotExist

class CategoryRepository(CategoryRepositoryPort):
    """
    Repository for managing categories in the database.
    """

    async def save(self, category: CategoryEntity) -> None:
        """
        Save a new category to the database.
        """
        await ModelCategory.create(
            cat_uuid=category.cat_uuid,
            cat_description=category.cat_description,
            cat_status=category.cat_status,
            cat_created=category.cat_created,
            cat_updated=category.cat_updated
        )

    async def get_by_description(self, description: str) -> Optional[CategoryEntity]:
        """
        Retrieve a category by its description.
        Returns None if not found.
        """
        try:
            model = await ModelCategory.filter(cat_description=description).first()
            if not model:
                return None
            return CategoryEntity(
                cat_uuid=model.cat_uuid,
                cat_description=model.cat_description,
                cat_status=model.cat_status,
                cat_created=model.cat_created,
                cat_updated=model.cat_updated
            )
        except DoesNotExist:
            return None

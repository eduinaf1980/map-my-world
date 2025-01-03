import uuid
from datetime import datetime
from uuid import UUID


class CategoryEntity:
    """
    Represents a Category entity with relevant details.
    """

    def __init__(self, cat_uuid: UUID, cat_description: str, cat_status: bool, cat_created: datetime,
                 cat_updated: datetime):
        """
        Initializes a CategoryEntity instance.

        :param cat_uuid: Unique identifier for the category.
        :param cat_description: Description of the category.
        :param cat_status: Status of the category (active/inactive).
        :param cat_created: The timestamp when the category was created.
        :param cat_updated: The timestamp of the last update (optional).
        """
        self.cat_uuid = cat_uuid
        self.cat_description = cat_description
        self.cat_status = cat_status
        self.cat_created = cat_created
        self.cat_updated = cat_updated

    @staticmethod
    def create(description: str) -> "CategoryEntity":
        """
        Creates a new CategoryEntity with the given description and default values for other attributes.

        :param description: Description of the new category.
        :return: A new CategoryEntity instance.
        """
        return CategoryEntity(
            cat_uuid=uuid.uuid4(),  # Generate a new unique UUID for the category
            cat_description=description,
            cat_status=True,  # Default to active status
            cat_created=datetime.utcnow(),  # Set the creation time to the current UTC time
            cat_updated=None  # No update timestamp at the time of creation
        )

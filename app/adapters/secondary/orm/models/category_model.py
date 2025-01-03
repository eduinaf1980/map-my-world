from tortoise import Model, fields
import uuid


class ModelCategory(Model):
    """
    Represents a Category in the system.

    Attributes:
    - `cat_uuid`: A unique identifier for the category (UUID).
    - `cat_description`: The description or name of the category (string).
    - `cat_status`: Indicates whether the category is active or inactive (boolean).
    - `cat_created`: The date and time when the category was created (datetime).
    - `cat_updated`: The date and time when the category was last updated (datetime).

    Meta:
    - The table name is set to `category` in the database.
    - The `cat_description` field has a unique constraint.
    - The `cat_created` field is indexed to optimize queries that filter by creation date.
    """

    # Unique identifier for the category
    cat_uuid = fields.UUIDField(pk=True, default=uuid.uuid4, description="Unique identifier for the category.")

    # Description or name of the category
    cat_description = fields.CharField(max_length=150, unique=True, null=False,
                                       description="Description / name of the category.")

    # Active or inactive status of the category
    cat_status = fields.BooleanField(null=False, description="Status of the category: Active or Inactive.")

    # The date when the category was created
    cat_created = fields.DatetimeField(auto_now_add=True, null=False, description="Creation date of the category.")

    # The date when the category was last updated
    cat_updated = fields.DatetimeField(null=True, description="Last update date of the category.")

    class Meta:
        # Table name and additional metadata
        table = 'category'
        comment = "Model for managing categories."

        # Indexes for optimization
        indexes = [
            ["cat_description"],  # Ensure the description is unique
            ["cat_created"]  # Index on creation date for quick lookups
        ]

        # Schema where the table belongs
        schema = "public"

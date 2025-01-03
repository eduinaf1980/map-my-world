from tortoise import Model, fields
import uuid

class ModelReview(Model):
    """
    Represents a review in the system.

    Attributes:
    - `rev_uuid`: A unique identifier for the review (UUID).
    - `rev_recommendation`: The recommendation text captured for the review (string).
    - `rev_obs`: Optional observations captured for the review (string).
    - `rev_created`: The date and time when the review was created (datetime).
    - `rev_fk_loc_uuid`: A foreign key to the Location model (UUID).
    - `rev_fk_cat_uuid`: A foreign key to the Category model (UUID).

    Meta:
    - The table name is set to `review` in the database.
    - The `rev_fk_loc_uuid`, `rev_fk_cat_uuid`, and `rev_created` fields are indexed together for quick lookups.
    - The `rev_created` field is indexed for filtering by creation date.
    """

    # Unique identifier for the review
    rev_uuid = fields.UUIDField(pk=True, default=uuid.uuid4, description="Unique identifier for the review.")

    # Recommendation captured for the review
    rev_recommendation = fields.CharField(max_length=500, unique=False, null=False, description="Recommendation captured for the review.")

    # Optional observations captured for the review
    rev_obs = fields.CharField(max_length=500, unique=False, null=True, description="Optional observations captured for the review.")

    # The date and time when the review was created
    rev_created = fields.DatetimeField(auto_now_add=True, null=False, description="Creation date of the review.")

    # Foreign key relationship to the Location model
    rev_fk_loc_uuid = fields.ForeignKeyField(
        'models.ModelLocation',
        related_name='locations',
        on_delete=fields.CASCADE,
        description="Relationship from review to location model."
    )

    # Foreign key relationship to the Category model
    rev_fk_cat_uuid = fields.ForeignKeyField(
        'models.ModelCategory',
        related_name='categories',
        on_delete=fields.CASCADE,
        description="Relationship from review to category model."
    )

    class Meta:
        # Table name and additional metadata
        table = 'review'
        comment = "Model for managing reviews with their recommendations."

        # Indexes for optimization
        indexes = [
            ["rev_fk_loc_uuid", "rev_fk_cat_uuid", "rev_created"],  # Ensure quick lookups for location, category, and creation date
            ["rev_created"]  # Index on creation date for efficient queries filtering by creation date
        ]

        schema = "public"
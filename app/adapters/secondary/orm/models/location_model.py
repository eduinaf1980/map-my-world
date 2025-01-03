from tortoise import Model, fields
import uuid


class ModelLocation(Model):
    """
    Represents a Location in the system.

    Attributes:
    - `loc_uuid`: A unique identifier for the location (UUID).
    - `loc_description`: A description or name of the location (string).
    - `loc_lat`: The latitude of the location (decimal).
    - `loc_long`: The longitude of the location (decimal).
    - `loc_status`: Indicates whether the location is active or inactive (boolean).
    - `loc_created`: The date and time when the location was created (datetime).
    - `loc_updated`: The date and time when the location was last updated (datetime).

    Meta:
    - The table name is set to `location` in the database.
    - The `loc_description` field is unique to ensure no duplicate locations.
    - The `loc_created` field is indexed to optimize queries filtering by creation date.
    """

    # Unique identifier for the location
    loc_uuid = fields.UUIDField(pk=True, default=uuid.uuid4, description="Unique identifier for the location.")

    # Description or name of the location
    loc_description = fields.CharField(max_length=150, unique=True, null=False,
                                       description="Description / name of the location.")

    # Latitude of the location
    loc_lat = fields.DecimalField(max_digits=9, null=True, decimal_places=6, description="Latitude of the location.")

    # Longitude of the location
    loc_long = fields.DecimalField(max_digits=9, null=True, decimal_places=6, description="Longitude of the location.")

    # Active or inactive status of the location
    loc_status = fields.BooleanField(null=False, description="Status of the location: Active or Inactive.")

    # The date when the location was created
    loc_created = fields.DatetimeField(auto_now_add=True, null=False, description="Creation date of the location.")

    # The date when the location was last updated
    loc_updated = fields.DatetimeField(null=True, description="Last update date of the location.")

    class Meta:
        # Table name and additional metadata
        table = 'location'
        comment = "Model for managing locations."

        # Indexes for optimization
        indexes = [
            ["loc_description"],  # Ensure the description is unique
            ["loc_created"]  # Index on creation date for quick lookups
        ]

        # Schema where the table belongs
        schema = "public"

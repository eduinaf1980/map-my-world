from marshmallow import Schema, fields, validates, ValidationError, pre_dump, post_dump

class BaseCategorySchema(Schema):
    """
    Schema for validating category data input (e.g., description).
    """
    description = fields.Str(required=True, description="Description of the category")

    @validates("description")
    def validate_description(self, value):
        """
        Validates that the description does not exceed 150 characters.
        """
        if len(value) > 150:
            raise ValidationError("Description cannot exceed 150 characters.")

class CategoryResponseSchema(Schema):
    """
    Schema for serializing category data in the response.
    """
    id = fields.UUID(attribute="cat_uuid", dump_only=True, metadata={"description": "Unique identifier of the category"})
    description = fields.Str(attribute="cat_description", dump_only=True, metadata={"description": "Category description"})
    status = fields.Boolean(attribute="cat_status", dump_only=True, metadata={"description": "Category status"})
    created = fields.DateTime(attribute="cat_created", dump_only=True, metadata={"description": "Creation date"})
    updated = fields.DateTime(attribute="cat_updated", dump_only=True, allow_none=True, metadata={"description": "Last updated date"})

    @pre_dump
    def prepare_data(self, data, **kwargs):
        """
        Prepares data for serialization.
        If the data is not a dictionary, it transforms it into one.
        """
        if isinstance(data, dict):
            return data
        return {
            "cat_uuid": data.cat_uuid,
            "cat_description": data.cat_description,
            "cat_status": data.cat_status,
            "cat_created": data.cat_created,
            "cat_updated": data.cat_updated,
        }

    @post_dump
    def clean_output(self, data, **kwargs):
        """
        Removes null or None values from the serialized output.
        """
        return {key: value for key, value in data.items() if value is not None}

from marshmallow import Schema, fields, validates, ValidationError, pre_dump, post_dump


class BaseReviewSchema(Schema):
    """
    Schema for validating review data input (e.g., recommendation, observations, category, and location).
    """
    # Recommendation for the review, required field
    recommendation = fields.Str(required=True, metadata={"description": "Recomendación de la revisión"})

    # Optional observations for the review
    obs = fields.Str(required=False, metadata={"description": "Observaciones de la revisión"})

    # Foreign key to Category, required field
    category = fields.UUID(required=True, metadata={"description": "Foránea a Categorías"})

    # Foreign key to Location, required field
    location = fields.UUID(required=True, metadata={"description": "Foránea a Ubicaciones"})

    @validates("recommendation")
    def validate_description(self, value):
        """
        Validates that the recommendation does not exceed 500 characters.
        """
        if len(value) > 500:
            raise ValidationError("La recomendación no puede exceder los 500 caracteres.")

    @validates("obs")
    def validate_description(self, value):
        """
        Validates that the observations do not exceed 500 characters.
        """
        if len(value) > 500:
            raise ValidationError("Las observaciones no pueden exceder los 500 caracteres.")


class ReviewResponseSchema(Schema):
    """
    Schema for serializing review response data, including UUID, recommendation, observations, and timestamps.
    """
    # UUID of the review, dumped only
    id = fields.UUID(attribute="rev_uuid", dump_only=True,
                     metadata={"description": "Identificador único de la revisión"})

    # Recommendation for the review, dumped only
    recommendation = fields.Str(attribute="rev_recommendation", dump_only=True,
                                metadata={"description": "Recomendación de la revisión"})

    # Optional observations for the review
    obs = fields.Boolean(attribute="rev_obs", dump_only=True,
                         metadata={"description": "Observaciones de la revisión - OPCIONAL"})

    # Creation date of the review, dumped only
    created = fields.DateTime(attribute="rev_created", dump_only=True, metadata={"description": "Fecha de creación"})

    # Foreign key to Category, dumped only
    category = fields.UUID(attribute="rev_fk_cat_uuid", dump_only=True,
                           metadata={"description": "Foránea a Categorías"})

    # Foreign key to Location, dumped only
    location = fields.UUID(attribute="rev_fk_loc_uuid", dump_only=True,
                           metadata={"description": "Foránea a Ubicaciones"})

    @pre_dump
    def prepare_data(self, data, **kwargs):
        """
        Prepares data for serialization.
        If the data is not already a dictionary, it transforms it into one with the required fields.
        """
        if isinstance(data, dict):
            return data
        return {
            "rev_uuid": data.rev_uuid,
            "rev_recommendation": data.rev_recommendation,
            "rev_obs": data.rev_obs,
            "rev_created": data.rev_created,
            "rev_fk_cat_uuid": data.rev_fk_cat_uuid,
            "rev_fk_loc_uuid": data.rev_fk_loc_uuid,
        }

    @post_dump
    def clean_output(self, data, **kwargs):
        """
        Removes null or None values from the serialized output.
        This ensures the response only contains fields with values.
        """
        return {key: value for key, value in data.items() if value is not None}

from marshmallow import Schema, fields, validates, ValidationError, pre_dump, post_dump


class BaseLocationSchema(Schema):
    """
    Schema for validating and serializing location data (e.g., description, latitude, and longitude).
    """
    # Description of the location, required field
    description = fields.Str(required=True, description="Descripción de la ubicación")

    # Latitude of the location, should be between -90 and 90
    lat = fields.Decimal(
        required=True,
        as_string=True,
        validate=lambda x: -90 <= x <= 90,  # Validates latitude range
        description="Latitud de la ubicación"
    )

    # Longitude of the location, should be between -180 and 180
    long = fields.Decimal(
        required=True,
        as_string=True,
        validate=lambda x: -180 <= x <= 180,  # Validates longitude range
        description="Longitud de la ubicación"
    )

    @validates("description")
    def validate_description(self, value):
        """
        Validates that the description does not exceed 150 characters.
        """
        if len(value) > 150:
            raise ValidationError("La descripción no puede exceder los 150 caracteres.")


class LocationResponseSchema(Schema):
    """
    Schema for serializing location response data, including UUID, description, lat/long, and status.
    """
    # UUID of the location, dumped only
    id = fields.UUID(attribute="loc_uuid", dump_only=True,
                     metadata={"description": "Identificador único de la ubicación"})

    # Description of the location, dumped only
    description = fields.Str(attribute="loc_description", dump_only=True,
                             metadata={"description": "Descripción de la ubicación"})

    # Status of the location (active or inactive), dumped only
    status = fields.Boolean(attribute="loc_status", dump_only=True, metadata={"description": "Estado de la ubicación"})

    # Creation date of the location, dumped only
    created = fields.DateTime(attribute="loc_created", dump_only=True, metadata={"description": "Fecha de creación"})

    # Last updated date of the location, dumped only, may be None
    updated = fields.DateTime(attribute="loc_updated", dump_only=True, allow_none=True,
                              metadata={"description": "Fecha de última modificación"})

    # Latitude of the location, dumped only
    lat = fields.Decimal(attribute="loc_lat", dump_only=True, metadata={"description": "Latitud de la ubicación"})

    # Longitude of the location, dumped only
    long = fields.Decimal(attribute="loc_long", dump_only=True, metadata={"description": "Longitud de la ubicación"})

    @pre_dump
    def prepare_data(self, data, **kwargs):
        """
        Prepares data for serialization.
        If the data is not already a dictionary, it transforms it into one with the required fields.
        """
        if isinstance(data, dict):
            return data
        return {
            "loc_uuid": data.loc_uuid,
            "loc_description": data.loc_description,
            "loc_status": data.loc_status,
            "loc_created": data.loc_created,
            "loc_updated": data.loc_updated,
            "loc_lat": data.loc_lat,
            "loc_long": data.loc_long
        }

    @post_dump
    def clean_output(self, data, **kwargs):
        """
        Removes null or None values from the serialized output.
        This ensures the response only contains fields with values.
        """
        return {key: value for key, value in data.items() if value is not None}

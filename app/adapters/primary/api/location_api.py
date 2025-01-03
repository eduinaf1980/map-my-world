from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from marshmallow import ValidationError
from app.adapters.secondary.orm.repositories.location_repository import LocationRepository
from app.core.application.usecases.create_location_usecase import CreateLocationUseCase
from app.adapters.primary.serializers.location_schema import BaseLocationSchema, LocationResponseSchema
from app.core.domain.exceptions.exceptions import DuplicateLocationError

router = APIRouter()

@router.post("/", response_model=dict)
async def create_location(location: dict):
    """
    Create a new location in the system.

    This endpoint allows users to create a new location by providing a description, latitude, and longitude.

    - **location**: A dictionary containing the description, latitude (lat), and longitude (long) of the location.

    **Response**:
    - Returns the created location with its unique identifier (loc_uuid), description, latitude, and longitude.

    **Error Handling**:
    - If the location already exists, a `400` status code with a `DuplicateLocationError` will be returned.
    - If the input data is invalid, a `400` status code with validation errors will be returned.

    Example request body:
    ```json
    {
      "description": "New Location",
      "lat": 40.712776,
      "long": -74.005974
    }
    ```

    Example response:
    ```json
    {
      "loc_uuid": "unique-uuid-here",
      "loc_description": "New Location",
      "loc_lat": 40.712776,
      "loc_long": -74.005974
    }
    ```
    """
    input_schema = BaseLocationSchema()
    try:
        # Validate the input data with BaseLocationSchema
        validated_data = input_schema.load(location)
    except ValidationError as err:
        # Return a 400 response with validation errors if the input data is invalid
        return JSONResponse(status_code=400, content={"errors": err.messages})

    # Instantiate the repository and use case for location creation
    repository = LocationRepository()
    use_case = CreateLocationUseCase(repository)
    try:
        # Execute the use case to create the location
        created_location = await use_case.execute(validated_data["description"], validated_data["lat"], validated_data["long"])

        # Serialize the response with LocationResponseSchema
        output_schema = LocationResponseSchema()
        return output_schema.dump(created_location)
    except DuplicateLocationError as e:
        # Raise an HTTP exception with status 400 if the location already exists
        raise HTTPException(status_code=400, detail=str(e))

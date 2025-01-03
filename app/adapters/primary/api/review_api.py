from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from marshmallow import ValidationError
from app.adapters.secondary.orm.repositories.review_repository import ReviewRepository
from app.core.application.usecases.create_review_usecase import CreateReviewUseCase
from app.adapters.primary.serializers.review_schema import BaseReviewSchema, ReviewResponseSchema

router = APIRouter()

@router.post("/", response_model=dict)
async def create_review(review: dict):
    """
    Create a new review in the system.

    This endpoint allows users to create a new review by providing a recommendation,
    category, location, and an optional observation.

    - **review**: A dictionary containing the review details. The dictionary must include:
        - **recommendation**: A string containing the review's recommendation.
        - **category**: The UUID of the category being reviewed.
        - **location**: The UUID of the location being reviewed.
        - **obs** (optional): Optional string field for additional observations.

    **Response**:
    - Returns the created review, including the UUID of the review and the provided recommendation.

    **Error Handling**:
    - If validation fails for the input data, a `400` status code with validation errors will be returned.
    - If any other error occurs, a `500` status code will be returned.

    Example request body:
    ```json
    {
      "recommendation": "Great place to visit!",
      "category": "unique-category-uuid",
      "location": "unique-location-uuid",
      "obs": "It is well maintained."
    }
    ```

    Example response:
    ```json
    {
      "rev_uuid": "unique-review-uuid",
      "rev_recommendation": "Great place to visit!",
      "rev_obs": "It is well maintained."
    }
    ```
    """
    input_schema = BaseReviewSchema()
    try:
        # Validate the input data with BaseReviewSchema
        validated_data = input_schema.load(review)
    except ValidationError as err:
        # Return a 400 response with validation errors if the input data is invalid
        return JSONResponse(status_code=400, content={"errors": err.messages})

    # Instantiate the repository and use case for review creation
    repository = ReviewRepository()
    use_case = CreateReviewUseCase(repository)
    try:
        # Execute the use case to create the review
        obs = validated_data.get("obs", "")  # Default to an empty string if 'obs' is not provided
        created_review = await use_case.execute(validated_data["recommendation"], validated_data["category"], validated_data["location"], obs)

        # Serialize the response with ReviewResponseSchema
        output_schema = ReviewResponseSchema()
        return output_schema.dump(created_review)
    except ValidationError as e:
        # Raise an HTTP exception with status 400 if the validation fails
        raise HTTPException(status_code=400, detail=str(e))

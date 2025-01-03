from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from marshmallow import ValidationError
from app.adapters.secondary.orm.repositories.category_repository import CategoryRepository
from app.core.application.usecases.create_category_usecase import CreateCategoryUseCase
from app.adapters.primary.serializers.category_schema import BaseCategorySchema, CategoryResponseSchema
from app.core.domain.exceptions.exceptions import DuplicateCategoryError

router = APIRouter()


@router.post("/", response_model=dict)
async def create_category(category: dict):
    """
    Create a new category in the system.

    This endpoint allows users to create a new category by providing a description.

    - **category**: A dictionary containing the description of the category.

    **Response**:
    - Returns the created category with its unique identifier and description.

    **Error Handling**:
    - If the category already exists, a `400` status code with a `DuplicateCategoryError` will be returned.
    - If the input data is invalid, a `400` status code with validation errors will be returned.

    Example request body:
    ```json
    {
      "description": "New Category"
    }
    ```

    Example response:
    ```json
    {
      "cat_uuid": "unique-uuid-here",
      "cat_description": "New Category"
    }
    ```
    """
    input_schema = BaseCategorySchema()
    try:
        # Validate the input data with BaseCategorySchema
        validated_data = input_schema.load(category)
    except ValidationError as err:
        # Return a 400 response with validation errors if the input data is invalid
        return JSONResponse(status_code=400, content={"errors": err.messages})

    # Instantiate the repository and use case for category creation
    repository = CategoryRepository()
    use_case = CreateCategoryUseCase(repository)
    try:
        # Execute the use case to create the category
        created_category = await use_case.execute(validated_data["description"])

        # Serialize the response with CategoryResponseSchema
        output_schema = CategoryResponseSchema()
        return output_schema.dump(created_category)
    except DuplicateCategoryError as e:
        # Raise an HTTP exception with status 400 if the category already exists
        raise HTTPException(status_code=400, detail=str(e))

from fastapi import APIRouter, HTTPException
from app.core.application.usecases.get_recommendation_usecase import GetRecommendationsUseCase
from app.adapters.secondary.orm.repositories.recommendation_repository import RecommendationRepository
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/", response_model=dict)
async def get_recommendations():
    """
    Retrieve a list of recommendations.

    This endpoint retrieves the latest 10 recommendations that are either unreviewed
    or have expired reviews (older than 30 days).

    **Response**:
    - Returns a list of recommendations with the location UUID, category UUID,
      and the flag indicating whether it's new, expired, or has been reviewed recently.

    **Error Handling**:
    - If there's an error during the process, a `500` status code with the error
      message will be returned.

    Example response:
    ```json
    {
      "recommendations": [
        {
          "loc_uuid": "unique-location-uuid",
          "cat_uuid": "unique-category-uuid",
          "bandera": 1,
          "review_date": "2023-12-10T00:00:00Z"
        },
        {
          "loc_uuid": "unique-location-uuid-2",
          "cat_uuid": "unique-category-uuid-2",
          "bandera": 2,
          "review_date": "2023-10-15T00:00:00Z"
        }
      ]
    }
    ```

    - **loc_uuid**: The UUID of the location.
    - **cat_uuid**: The UUID of the category.
    - **bandera**: A flag indicating the state of the review:
      - `1`: Never reviewed.
      - `2`: Review expired (older than 30 days).
      - `0`: Recently reviewed.
    - **review_date**: The date of the last review, or null if never reviewed.
    """
    # Instanciamos el repositorio y el caso de uso
    recommendation_repository = RecommendationRepository()
    use_case = GetRecommendationsUseCase(recommendation_repository)

    try:
        # Ejecutar el caso de uso para obtener las recomendaciones
        recommendations = await use_case.execute()

        # Convertir las recomendaciones a un formato serializable (diccionario)
        recommendations_dict = [rec.dict() for rec in recommendations]

        return JSONResponse(content={"recommendations": recommendations_dict})
    except Exception as e:
        # En caso de error, lanzar una excepción HTTP
        raise HTTPException(status_code=500, detail=str(e))






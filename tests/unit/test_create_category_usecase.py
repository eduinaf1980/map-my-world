import pytest
from unittest.mock import AsyncMock
from datetime import datetime
from app.core.application.usecases.create_category_usecase import CreateCategoryUseCase
from app.core.domain.entities.category_entity import CategoryEntity
from app.core.domain.exceptions.exceptions import DuplicateCategoryError


@pytest.mark.asyncio
async def test_create_category_success():
    # Mock del repositorio
    mock_repository = AsyncMock()
    mock_repository.get_by_description.return_value = None
    mock_repository.save.return_value = None

    # Caso de uso
    use_case = CreateCategoryUseCase(mock_repository)

    # Ejecutar el caso de uso
    category = await use_case.execute("Books")

    # Verificar resultados
    assert isinstance(category, CategoryEntity)
    assert category.cat_description == "Books"
    assert category.cat_status is True
    mock_repository.get_by_description.assert_awaited_once_with("Books")
    mock_repository.save.assert_awaited_once_with(category)


@pytest.mark.asyncio
async def test_create_category_duplicate():
    # Mock del repositorio
    mock_repository = AsyncMock()
    mock_repository.get_by_description.return_value = CategoryEntity(
        cat_uuid="1234",
        cat_description="Books",
        cat_status=True,
        cat_created=datetime.utcnow(),
        cat_updated=None,  # Incluir cat_updated con valor None
    )

    # Caso de uso
    use_case = CreateCategoryUseCase(mock_repository)

    # Ejecutar el caso de uso y verificar que lanza una excepción
    with pytest.raises(DuplicateCategoryError):
        await use_case.execute("Books")

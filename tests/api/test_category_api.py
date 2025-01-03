import pytest

@pytest.mark.asyncio
async def test_create_category_api_success(test_client):
    category_data = {"description": "Books"}

    response = test_client.post("/categories/", json=category_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["description"] == "Books"
    assert "id" in response_data
    assert response_data["status"] is True


@pytest.mark.asyncio
async def test_create_category_api_duplicate(test_client):
    category_data = {"description": "Books"}

    # Crear categoría
    test_client.post("/categories/", json=category_data)

    # Intentar duplicar
    response_duplicate = test_client.post("/categories/", json=category_data)

    assert response_duplicate.status_code == 400
    assert response_duplicate.json()["detail"] == "A category with this description already exists."

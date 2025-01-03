import pytest
from tortoise.contrib.test import initializer, finalizer
import os

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """
    Inicializa Tortoise ORM para los tests.
    Configura una base de datos SQLite en memoria para pruebas.
    """
    environment = os.getenv("ENVIRONMENT", "testing")

    if environment != "testing":
        raise RuntimeError("Tests deben ejecutarse en el entorno 'testing'.")

    initializer(
        modules={"models": ["app.adapters.secondary.orm.models"]},  # Ruta a los modelos
        db_url="sqlite://:memory:",  # Base de datos en memoria
        app_label="models",  # Alias para los modelos
    )
    yield
    finalizer()


@pytest.fixture
def test_client():
    """
    Devuelve un cliente de pruebas para la aplicación FastAPI.
    """
    from fastapi.testclient import TestClient
    from app.main_app.main import app

    return TestClient(app)


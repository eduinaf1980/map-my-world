from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.main_app.config import DATABASE_URL
from app.adapters.primary.api.category_api import router as category_router
from app.adapters.primary.api.location_api import router as location_router
from app.adapters.primary.api.review_api import router as review_router
from app.adapters.primary.api.recommendation_api import router as recommendation_route
import os

# Environment configuration: This allows you to set the environment dynamically (production, development, etc.)
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

# FastAPI application instance
app = FastAPI(
    title="MapMyWorld API",  # Title of the API
    description="API for managing categories, locations, recommendations, and reviews.",  # Short description of the API functionality
    version="1.0.0",  # Version of the API
)

# Include category routes
# This will allow you to manage category-related operations (e.g., create, read, update, delete categories)
app.include_router(category_router, prefix="/categories", tags=["Categories"])

# Include location routes
# This will allow you to manage location-related operations (e.g., create, read, update, delete locations)
app.include_router(location_router, prefix="/locations", tags=["Locations"])

# Include review routes
# This will allow you to manage review-related operations (e.g., create, read, update, delete reviews)
app.include_router(review_router, prefix="/reviews", tags=["Reviews"])

# Include recommendation routes
# This will allow you to manage recommendation-related operations (e.g., get recommendations)
app.include_router(recommendation_route, prefix="/recommendations", tags=["Recommendations"])

# Tortoise ORM configuration for connecting to the database and managing models
# This connects the FastAPI app to the database using the Tortoise ORM, defines the models to use, and generates schemas if in development environment
register_tortoise(
    app,
    db_url=DATABASE_URL,  # Database URL, should be defined in the configuration file (e.g., DATABASE_URL in .env)
    modules={"models": ["app.adapters.secondary.orm.models"]},  # Define the models module
    generate_schemas=ENVIRONMENT == "development",  # Automatically generate schemas if in development
    add_exception_handlers=True,  # Adds exception handling for common Tortoise ORM errors
)

# Basic root route for testing the API and ensuring the service is up and running
@app.get("/")
async def read_root():
    return {"message": "Welcome to MapMyWorld API"}  # Simple message for the root endpoint


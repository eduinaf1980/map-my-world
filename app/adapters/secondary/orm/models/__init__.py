from .category_model import ModelCategory
from .location_model import ModelLocation
from .review_model import ModelReview

# Esto asegura que Tortoise pueda detectar los modelos correctamente.
__all__ = ["ModelCategory", "ModelLocation", "ModelReview"]

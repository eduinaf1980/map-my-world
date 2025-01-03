import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgres://postgres:postgres@db:5432/mapmyworld")

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.adapters.secondary.orm.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
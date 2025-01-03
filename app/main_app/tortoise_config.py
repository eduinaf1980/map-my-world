TORTOISE_ORM = {
    "development": {
        "connections": {"default": "sqlite://db.sqlite3"},  # Base de datos SQLite para desarrollo
        "apps": {
            "models": {
                "models": ["app.adapters.secondary.orm.models"],
                "default_connection": "default",
            },
        },
    },
    "testing": {
        "connections": {"default": "sqlite://:memory:"},  # Base de datos en memoria para pruebas
        "apps": {
            "models": {
                "models": ["app.adapters.secondary.orm.models"],
                "default_connection": "default",
            },
        },
    },
    "production": {
        "connections": {"default": "postgres://user:password@localhost/dbname"},  # Cambia por tu configuración de producción
        "apps": {
            "models": {
                "models": ["app.adapters.secondary.orm.models"],
                "default_connection": "default",
            },
        },
    },
}

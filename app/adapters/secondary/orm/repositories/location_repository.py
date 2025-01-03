from typing import Optional
from app.core.domain.entities.location_entity import LocationEntity
from app.core.domain.ports.location_ports import LocationRepositoryPort
from app.adapters.secondary.orm.models.location_model import ModelLocation
from tortoise.exceptions import DoesNotExist

class LocationRepository(LocationRepositoryPort):
    """
    Repository for managing location data in the database.
    """

    async def save(self, location: LocationEntity) -> None:
        """
        Save a new location to the database.
        """
        await ModelLocation.create(
            loc_uuid=location.loc_uuid,
            loc_description=location.loc_description,
            loc_status=location.loc_status,
            loc_created=location.loc_created,
            loc_updated=location.loc_updated,
            loc_lat=location.loc_lat,
            loc_long=location.loc_long
        )

    async def get_by_description(self, description: str) -> Optional[LocationEntity]:
        """
        Retrieve a location by its description.
        Returns None if not found.
        """
        try:
            model = await ModelLocation.filter(loc_description=description).first()
            if not model:
                return None
            return LocationEntity(
                loc_uuid=model.loc_uuid,
                loc_description=model.loc_description,
                loc_status=model.loc_status,
                loc_created=model.loc_created,
                loc_updated=model.loc_updated,
                loc_lat=model.loc_lat,
                loc_long=model.loc_long
            )
        except DoesNotExist:
            return None

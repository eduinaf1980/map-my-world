from app.core.domain.entities.location_entity import LocationEntity
from app.core.domain.ports.location_ports import LocationRepositoryPort
from app.core.domain.exceptions.exceptions import DuplicateLocationError
from decimal import Decimal


class CreateLocationUseCase:
    """
    Use case for creating a new location.
    """

    def __init__(self, repository: LocationRepositoryPort):
        """
        Initializes the use case with the provided location repository.
        """
        self.repository = repository

    async def execute(self, description: str, lat: Decimal, long: Decimal) -> LocationEntity:
        """
        Creates a new location if no location exists with the given description.
        """
        # Check if location exists
        existing_location = await self.repository.get_by_description(description)
        if existing_location:
            raise DuplicateLocationError("A location with this description already exists.")

        # Create and save the new location
        location = LocationEntity.create(description, lat, long)
        await self.repository.save(location)

        return location


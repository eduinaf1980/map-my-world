from abc import ABC, abstractmethod
from typing import Optional
from app.core.domain.entities.location_entity import LocationEntity


class LocationRepositoryPort(ABC):
    """
    Abstract base class for the Location repository port, defining the methods
    that should be implemented for interacting with location data.
    """

    @abstractmethod
    async def save(self, location: LocationEntity) -> None:
        """
        Save a location entity.

        :param location: The location entity to be saved.
        """
        pass

    @abstractmethod
    async def get_by_description(self, description: str) -> Optional[LocationEntity]:
        """
        Retrieve a location by its description.

        :param description: The description of the location to be fetched.
        :return: An optional LocationEntity if found, otherwise None.
        """
        pass

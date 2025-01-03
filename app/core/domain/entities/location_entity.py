import uuid
from datetime import datetime
from uuid import UUID
from decimal import Decimal

class LocationEntity:
    """
    Represents a location entity with relevant details such as its coordinates, description, and status.
    """

    def __init__(self, loc_uuid: UUID, loc_description: str, loc_lat: Decimal, loc_long: Decimal, loc_status: bool, loc_created: datetime, loc_updated: datetime):
        """
        Initializes a LocationEntity instance.

        :param loc_uuid: Unique identifier for the location.
        :param loc_description: Description of the location.
        :param loc_lat: Latitude of the location.
        :param loc_long: Longitude of the location.
        :param loc_status: Status of the location (active/inactive).
        :param loc_created: The timestamp when the location was created.
        :param loc_updated: The timestamp of the last update (optional).
        """
        self.loc_uuid = loc_uuid
        self.loc_description = loc_description
        self.loc_status = loc_status
        self.loc_created = loc_created
        self.loc_updated = loc_updated
        self.loc_lat = loc_lat
        self.loc_long = loc_long

    @staticmethod
    def create(description: str, lat: Decimal, long: Decimal) -> "LocationEntity":
        """
        Creates a new LocationEntity with the given description, latitude, and longitude.

        :param description: Description of the new location.
        :param lat: Latitude of the new location.
        :param long: Longitude of the new location.
        :return: A new LocationEntity instance.
        """
        return LocationEntity(
            loc_uuid=uuid.uuid4(),  # Generate a new unique UUID for the location
            loc_description=description,
            loc_status=True,  # Default to active status
            loc_created=datetime.utcnow(),  # Set the creation time to the current UTC time
            loc_updated=None,  # No update timestamp at the time of creation
            loc_lat=lat,  # Latitude of the location
            loc_long=long  # Longitude of the location
        )

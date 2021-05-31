from dateutil import parser as dateparser
from datetime import datetime

class LocalUser:
    def __init__(self, data: dict):
        self._data = data
    
    @property
    def name(self) -> str:
        return self._data.get("username")
    
    @property
    def ship_count(self) -> int:
        return self._data.get("shipCount")

    @property
    def structure_count(self) -> int:
        return self._data.get("structureCount")

    @property
    def joined_at(self) -> datetime:
        return dateparser.parse(self._data.get("joinedAt"))
    
    @property
    def credits(self) -> int:
        return self._data.get(self._data.get("credits"))


    
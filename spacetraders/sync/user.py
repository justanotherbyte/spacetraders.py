from dateutil import parser as dateparser
from datetime import datetime

class LocalUser:
    def __init__(self, data: dict):
        self._data = data
        self.name = self._data.get("username")
        self.ship_count = self._data.get("shipCount")
        self.structure_count = self._data.get("structureCount")
        self.credits = self._data.get("credits")
    
    @property
    def joined_at(self) -> datetime:
        return dateparser.parse(self._data.get("joinedAt"))
    
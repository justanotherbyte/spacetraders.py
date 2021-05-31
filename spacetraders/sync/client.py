from .http import HTTPClient
from .user import LocalUser

from typing import Optional

class SyncClient:
    def __init__(self):
        self.http = HTTPClient()
        self._user = None

    @property
    def user(self) -> Optional[LocalUser]:
        if self._user is None:
            return None

        return self._user


    def login(self, token: str) -> dict:
        self.http.token = token.strip()
        data = self.http.connect(login = True)
        self._user = LocalUser(data.get("user"))
        return data

    def create_account(self, username: str) -> dict:
        data = self.http.connect(username = username)
        self._user = LocalUser(data.get("user"))
        return data

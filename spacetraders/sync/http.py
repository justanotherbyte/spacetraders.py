import requests
import sys
from .errors import HTTPException

__version__ = "0.1.0a"

class Route:
    BASE = "https://api.spacetraders.io"
    def __init__(self, endpoint: str, method: str = "GET", **params):
        self.endpoint = endpoint.format(**params)
        self.method = method
        self.url = self.BASE + self.endpoint


class HTTPClient:
    def __init__(self):
        self.__session = None # filled in self.connect
        self.token = None
        self.username = None
        
        user_agent = 'SyncClient (https://github.com/muunie/spacetraders.py {0}) Python/{1[0]}.{1[1]} requests/{2}'
        self.user_agent = user_agent.format(__version__, sys.version_info, requests.__version__)

    def request(self, route: Route, **kwargs) -> dict:
        method = route.method
        url = route.url

        headers = {
            "Content-Type": "application/json",
            "User-Agent": self.user_agent
        }

        if self.token:
            headers["Authorization"] = "Bearer " + self.token

        kwargs["headers"] = headers
        resp = self.__session.request(method, url, **kwargs)
        status = resp.status_code
        if 300 > status >= 200:
            return resp.json()

        raise HTTPException(status, resp.reason) # some sort of HTTP error occured. Raises an exception.



    def connect(self, *, login: bool = False, username: str = None):
        self.__session = requests.Session()
        if login:
            route = Route("/my/account")
            data = self.request(route)
            return data

        if not username:
            raise ValueError("No Username Set")

        route = Route("/users/{username}/claim", "POST", username = username)
        data = self.request(route)
        return data

        



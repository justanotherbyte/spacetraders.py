import requests
import sys
from . import __version__
from .errors import HTTPException

class Route:
    BASE = "https://api.spacetraders.io"
    def __init__(self, endpoint: str, method: str = "GET", **params):
        self.endpoint = endpoint.format(**params)
        self.method = method
        self.url = self.BASE + self.endpoint


class HTTPClient:
    def __init__(self):
        self.__session = requests.Session() # filled in self.connect
        self.token = None
        self.username = None
        
        user_agent = 'SyncClient (https://github.com/muunie/spacetraders.py {0}) Python/{1[0]}.{1[1]} requests/{2}'
        self.user_agent = user_agent.format(__version__, sys.version_info, requests.__version__)

    def request(self, route: Route, **kwargs) -> dict:
        method = route.method
        url = route.url

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": self.user_agent
        }

        kwargs["headers"] = headers
        resp = self.__session.request(route.method, route.url, **kwargs)
        status = resp.status_code
        if 300 > status >= 200:
            return resp.json()

        if status == 429:
            # rip we're being ratelimited
            raise HTTPException(status, "Ratelimit Exceeded")



    def connect(self, *, login: bool = False):
        if login:
            route = Route("/my/account")



    
        


    

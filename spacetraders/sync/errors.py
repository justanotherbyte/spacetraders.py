
class HTTPException(Exception):
    def __init__(self, status: int, reason: str):
        self.status = status
        self.reason = reason

    def __str__(self):
        return "HTTPException: {}: {}".format(self.status, self.reason)
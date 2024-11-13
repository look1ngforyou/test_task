import json
import requests
import curlify
from utilities.json_utilities import JsonUtils
from my_logger.logger import Logger


def log_response(function):
    """Decorator to log request and response details."""

    def _log_response(*args, **kwargs) -> requests.Response:
        response = function(*args, **kwargs)
        Logger.info(f"Request curl: {curlify.to_curl(response.request)}")
        body = (
            json.dumps(response.json(), indent=4)
            if JsonUtils.is_json(response.text) else response.text
        )
        Logger.info(f"Response status code={response.status_code}, elapsed time={response.elapsed}\n\n{body}\n")
        return response

    return _log_response


class ApiUtilities:
    """A utility class for making API requests with logging support."""

    def __init__(self, url, headers=None):
        """Initialize the ApiUtilities with a base URL"""
        if headers is None:
            headers = {}
        self.url = url
        self.session = requests.Session()
        self.session.headers = headers

    @log_response
    def get(self, endpoint_url=None, **kwargs) -> requests.Response:
        """Send a GET request to the specified endpoint."""
        response = self.session.get(self.url + endpoint_url, **kwargs)
        return response

    @log_response
    def post(self, endpoint_url, data=None, json=None, **kwargs) -> requests.Response:
        """Send a POST request to the specified endpoint."""
        response = self.session.post(self.url + endpoint_url, data=data, json=json, **kwargs)
        return response

    def update_headers(self, headers: dict) -> None:
        self.session.headers.update(headers)

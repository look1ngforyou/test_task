import json
from uuid import UUID
import requests
from utilities.api_utilities import ApiUtilities


class ApiHelper:
    """
    Helper class to perform API requests and handle raw (HTTP status codes, headers, cookies, elapsed, encoding etc)
    responses.
    """
    API_REQUEST_ADDRESS = 'some_url_endpoint/'

    def __init__(self, api_utilities: ApiUtilities):
        """
        Initialize the ApiHelper with ApiUtilities.

        Args:
            api_utilities (ApiUtilities): Utility instance for making API requests.
        """
        self.api_utilities = api_utilities

    def get_result_request(self, user_id: UUID) -> requests.Response:
        """
        Send a GET request to retrieve data for a specific UUID.

        Args:
            user_id (UUID): The UUID of the user to fetch data for.

        Returns:
            requests.Response: Raw response from the API.
        """
        response = self.api_utilities.get(self.API_REQUEST_ADDRESS + str(user_id))
        return response

    def post_palindrome_request(self, json_body: json) -> requests.Response:
        """
        Send a POST request to submit a palindrome check.

        Args:
            json_body (json): JSON body containing the data to check for a palindrome.

        Returns:
            requests.Response: Raw response from the API.
        """
        response = self.api_utilities.post(self.API_REQUEST_ADDRESS, json=json_body)
        return response

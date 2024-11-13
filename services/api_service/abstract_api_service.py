from uuid import UUID
from services.api_service.helper.api_helper import ApiHelper
from services.api_service.models.get_response_model import GetMethodRequestResponse
from services.api_service.models.post_palindrome_model import PostPalindromeModel
from services.api_service.models.post_request_response_model import PostRequestResponseModel
from utilities.api_utilities import ApiUtilities


class AbstractApiService:
    """
    Abstract service class to perform API requests with response validation.
    """

    def __init__(self, api_utilities: ApiUtilities):
        """
        Initialize the AbstractApiService with ApiUtilities and ApiHelper.

        Args:
            api_utilities (ApiUtilities): Utility instance for making API requests.
        """
        self.api_utilities = api_utilities
        self.api_helper = ApiHelper(api_utilities)

    def get_result(self, user_id: UUID) -> GetMethodRequestResponse:
        """
        Retrieve data for a specific UUID and return a validated response model.

        This method uses the `ApiHelper` to send a GET request to the relevant endpoint,
        then parses the raw response JSON into a `GetMethodRequestResponse` model.

        Args:
            user_id (UUID): The UUID of the user to retrieve.

        Returns:
            GetMethodRequestResponse: An instance of `GetMethodRequestResponse` containing
            validated data parsed from the raw API response.
        """
        response = self.api_helper.get_result_request(user_id=user_id)
        return GetMethodRequestResponse(**response.json())

    def post_palindrome(self, palindrome: PostPalindromeModel) -> PostRequestResponseModel:
        """
        Submit a palindrome check request and return a validated response model.

        This method uses the `ApiHelper` to send a POST request with a JSON payload derived from
        the `PostPalindromeModel` input. The raw API response is then parsed into a
        `PostRequestResponseModel`.

        Args:
            palindrome (PostPalindromeModel): Instance containing the data for the palindrome check.

        Returns:
            PostRequestResponseModel: Instance of `PostRequestResponseModel` with validated data parsed
            from the raw API response.
        """
        response = self.api_helper.post_palindrome_request(json_body=palindrome.model_dump())
        return PostRequestResponseModel(**response.json())

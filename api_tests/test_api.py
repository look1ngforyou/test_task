import pytest
from faker import Faker
from my_logger.logger import Logger


class TestAPI:
    def test_get_request(self, abs_api_service):
        """
        Test the GET request for a specific UUID.

        Steps:
        1. Generate a random UUID using Faker.
        2. Send a GET request to retrieve data for that UUID.
        3. Assert that the response matches the expected UUID string.

        Notes:
        - `abs_api_service.get_uuid(user_id=random_uuid)` is expected to return a response that
          contains the same UUID as a string, which is stored in `expected_response`.
        - The assertion checks that the actual response matches the expected UUID string,
          ensuring the API returns the correct data for the requested UUID.
        """
        Logger.info(" !!! Step 1: Generate a random UUID")
        random_uuid = Faker().uuid4()

        Logger.info(" !!! Step 2: Send GET request")
        actual_response = abs_api_service.get_result(user_id=random_uuid)

        Logger.info(" !!! Step 3: Assert the response")
        expected_response = str(random_uuid)
        assert expected_response == actual_response, f"Expected {expected_response}, got {actual_response} instead"

    @pytest.mark.parametrize("palindrome_value", [True, False])
    def test_post_request(self, abs_api_service, palindrome_value):
        """
        Test the POST request with a palindrome check.

        Steps:
        1. Define input data based on the `palindrome_value` parameter.
           - If `palindrome_value` is `True`, use a palindrome string.
           - If `palindrome_value` is `False`, use a non-palindromic string.
        2. Send a POST request with the defined palindrome data.
        3. Assert the response:
           - If `palindrome_value` is `True`, the result should be a palindrome.
           - If `palindrome_value` is `False`, the result should not be a palindrome.

        Notes:
        - `abs_api_service.post_palindrome(palindrome=palindrome_value)` sends the palindrome data and returns
          a response with a `result` field in it.
        - Then assert that the `result` matches the expected palindrome behavior based on `palindrome_value`.
        """
        Logger.info(" !!! Step 1 - Send post request")
        actual_response = abs_api_service.post_palindrome(palindrome=palindrome_value)

        Logger.info(" !!! Step 2: Assert the response")
        result = actual_response.result
        if palindrome_value:
            # Expect result to be a palindrome if palindrome_value is True
            assert result == result[::-1], f"Expected a palindrome in result, got '{result}'"
        else:
            # Expect result to be non-palindromic if palindrome_value is False
            assert result != result[::-1], f"Expected a non-palindrome in result, got '{result}'"

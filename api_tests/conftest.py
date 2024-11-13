import pytest
from utilities.api_utilities import ApiUtilities
from services.api_service.abstract_api_service import AbstractApiService


@pytest.fixture(scope="function")
def abs_api_service():
    """
    Pytest fixture for AbstractApiService for further re-use in tests
    """
    api_utilities = ApiUtilities(url="some_url")

    return AbstractApiService(api_utilities=api_utilities)

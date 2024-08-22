import pytest
import allure
import requests

@allure.title("Test Get request - restful booker project#1")
@allure.description("TC#1-->verify that get request with id works")
@allure.tag("regression","p0","smoke")
@allure.label("owner","himanth")
@allure.testcase("TC5")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200
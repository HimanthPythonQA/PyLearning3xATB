import pytest
import allure
import requests

@allure.title("Test Get request - restful booker project#1")
@allure.description("TC#1-->verify that get request with id works")
@allure.tag("regression","p0","smoke")
@allure.label("owner","himanth")
@allure.testcase("TC1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200


@allure.title("Test Get request - restful booker project#1")
@allure.description("TC#2->verify that get request with invalid working bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404

@allure.title("Test Get request - restful booker project#1")
@allure.description("TC#3->verify that get request with invalid working bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    assert responseData.status_code == 404
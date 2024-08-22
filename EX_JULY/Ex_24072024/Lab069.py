# for post request
import pytest
import allure
import requests


@allure.title("Create booking CRUD")
@allure.description("TC#1-->verify the create booking")
@pytest.mark.crud
def test_create_booking_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "sally",
        "lastname": "brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData = response.json()

    assert "bookingid" in responseData
    assert isinstance(responseData["bookingid"], int)
    assert responseData["bookingid"] > 0
    firstname = responseData["booking"]["firstname"]
    totalprice = responseData["booking"]["totalprice"]
    assert firstname == "sally"
    assert totalprice == 111

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"



@allure.title("Create booking CRUD")
@allure.description("TC#1-->verify the create booking")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))


    assert response.status_code == 500
# for put request we need URL/path-param/token--auth/payload
import requests
import allure
import pytest


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type: application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


def create_booking():
    print("create booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {

        "firstname": "Himanth",
        "lastname": "brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",  # Corrected comma issue
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Himanth",  # Updated to match your assertion
        "lastname": "brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Himanth"


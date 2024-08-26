import requests
import pytest


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(f"Generated token: {token}")
    return token


def create_booking():
    print("Create booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
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
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Booking ID: {booking_id}")
    return booking_id


def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    booking_id = create_booking()
    PUT_URL = f"{base_url}/booking/{booking_id}"

    token = create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    json_payload = {
        "firstname": "himanth",
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
    assert data["firstname"] == "himanth"
    print("PUT request passed successfully.")


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = f"{URL}{booking_id}"
    token = create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    print(f"DELETE Request Headers: {headers}")
    response = requests.delete(url=DELETE_URL, headers=headers)





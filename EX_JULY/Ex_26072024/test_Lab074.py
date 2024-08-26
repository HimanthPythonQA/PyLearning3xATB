import pytest
import requests
import allure

@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print("Generated token:", token)
    return token


@pytest.fixture()
def create_booking_id():
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
    data = response.json()
    booking_id = data["bookingid"]  # Corrected key
    print("Generated booking ID:", booking_id)
    return booking_id


def test_update_req1(create_token, create_booking_id):
    print("Token-->", create_token)
    print("bookingId-->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    PUT_URL = f"{base_url}/booking/{create_booking_id}"  # No need to call create_booking_id()

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={create_token}"  # No need to call create_token()
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


def test_update_req2(create_token, create_booking_id):
    print("Token-->", create_token)
    print("bookingId-->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    PUT_URL = f"{base_url}/booking/{create_booking_id}"  # No need to call create_booking_id()

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={create_token}"  # No need to call create_token()
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


# Run the tests
if __name__ == "__main__":
    pytest.main()

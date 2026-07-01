import pytest
from helpers.helpers import generate_random_string
from api.courier_api import CourierAPI
from api.order_api import OrderAPI
from datetime import datetime, timedelta


@pytest.fixture
def create_and_delete_courier():
    courier_data = CourierAPI.register_new_courier_and_return_login_password()
    login, password, first_name = courier_data
    response = CourierAPI.login_courier(login, password)
    courier_id = response.json()["id"]
    yield {"login": login, "password": password, "first_name": first_name, "id": courier_id}
    CourierAPI.delete_courier(courier_id)

@pytest.fixture
def create_order():
    delivery_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
    payload = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "ул. Ленина 1",
        "metroStation": 1,
        "phone": "+79991234567",
        "rentTime": 1,
        "deliveryDate": delivery_date,
        "comment": "Тестовый заказ"
    }
    response = OrderAPI.create_order(payload)
    track = response.json().get("track")
    return track

@pytest.fixture
def create_courier_and_get_id():
    login = generate_random_string(10)
    password = generate_random_string(10)
    CourierAPI.create_courier(login, password)
    login_response = CourierAPI.login_courier(login, password)
    courier_id = login_response.json()["id"]
    yield {"id": courier_id, "login": login, "password": password}
    try:
        CourierAPI.delete_courier(courier_id)
    except:
        pass

@pytest.fixture
def courier_cleanup():
    couriers = []
    yield couriers
    for login, password in couriers:
        try:
            resp = CourierAPI.login_courier(login, password)
            if resp.status_code == 200:
                courier_id = resp.json()["id"]
                CourierAPI.delete_courier(courier_id)
        except Exception:
            pass

import pytest
from constants import ResponseCode
from api.order_api import OrderAPI
from data.test_data import ORDER_DATA
import allure
from datetime import datetime, timedelta

@allure.epic("Тестирование API заказов")
@allure.feature("Создание заказа")
class TestOrderCreate:

    @allure.title("Создание заказа с разными вариантами цвета")
    @allure.description("Проверка, что можно указать BLACK, GREY, оба цвета или не указывать цвет")
    @pytest.mark.parametrize("order_color", ORDER_DATA)
    def test_create_order_with_colors(self, order_color):
        delivery_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
        payload = {
            "firstName": "Иван",
            "lastName": "Кузиков",
            "address": "ул. Ленина 1",
            "metroStation": 1,
            "phone": "+79991234567",
            "rentTime": 1,
            "deliveryDate": delivery_date,
            "comment": "Тестовый заказ",
            **order_color
            }
        response = OrderAPI.create_order(payload)
        assert response.status_code == ResponseCode.CREATED
        assert "track" in response.json()

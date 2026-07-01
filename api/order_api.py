import requests
from constants import URL, Endpoints
import allure

class OrderAPI:
    
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(URL.BASE_URL + Endpoints.ORDERS, json=payload)
    
    @staticmethod
    @allure.step("Получить список всех заказов")
    def get_orders():
        return requests.get(URL.BASE_URL + Endpoints.ORDERS)
    
    @staticmethod
    @allure.step("Принять заказ с id '{order_id}' для курьера '{courier_id}'")
    def accept_order(order_id, courier_id):
        return requests.put(
            f"{URL.BASE_URL}{Endpoints.ORDER_ACCEPT}/{order_id}",
            params={"courierId": courier_id}
        )
    
    @staticmethod
    @allure.step("Получить заказ по треку '{track_number}'")
    def get_order_by_track(track_number):
        return requests.get(
            f"{URL.BASE_URL}{Endpoints.ORDER_TRACK}",
            params={"t": track_number}
        )

import requests
from constants import URL, Endpoints
import allure

class CourierAPI:

    @staticmethod
    @allure.step("Создать курьера с логином '{login}'")
    def create_courier(login, password, first_name=None):
        payload = {"login": login, "password": password}
        if first_name:
            payload["firstName"] = first_name
        return requests.post(URL.BASE_URL + Endpoints.COURIER, data=payload)
    
    @staticmethod
    @allure.step("Авторизоваться под курьером с логином '{login}'")
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        return requests.post(URL.BASE_URL + Endpoints.LOGIN, data=payload)

    @staticmethod
    @allure.step("Удалить курьера с id '{courier_id}'")
    def delete_courier(courier_id):
        return requests.delete(f"{URL.BASE_URL}{Endpoints.COURIER}/{courier_id}")
    
    @staticmethod
    @allure.step("Отправить запрос на удаление курьера без id")
    def delete_courier_without_id():
        return requests.delete(f"{URL.BASE_URL}{Endpoints.COURIER}")

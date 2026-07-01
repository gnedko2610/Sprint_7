import requests
from constants import URL, Endpoints
from helpers.helpers import generate_random_string
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
    @allure.step("Зарегистрировать нового курьера и вернуть логин/пароль")
    def register_new_courier_and_return_login_password():
        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(URL.BASE_URL + Endpoints.COURIER, data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass
    
    @staticmethod
    @allure.step("Создать курьера с логином '{login}' и зарегистрировать для удаления")
    def create_courier_with_cleanup(login, password, first_name, cleanup_list):
        payload = {"login": login, "password": password}
        if first_name:
            payload["firstName"] = first_name
        response = requests.post(URL.BASE_URL + Endpoints.COURIER, data=payload)

        # Если создание успешно, добавляем курьера в список очистки
        if response.status_code == 201:
            cleanup_list.append((login, password))
        return response
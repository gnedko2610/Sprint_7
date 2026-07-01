from constants import ResponseCode, ErrorMessages
from helpers.helpers import register_new_courier_and_return_login_password, generate_random_string
from api.courier_api import CourierAPI
import allure


@allure.epic("Тестирование API курьера")
@allure.feature("Создание курьера")
class TestCourierCreate:

    @allure.title("Успешное создание курьера")
    @allure.description("Проверка, что курьера можно создать с корректными данными")
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierAPI.create_courier(login, password, first_name)
        assert response.status_code == ResponseCode.CREATED
        assert response.json() == {"ok": True}

    @allure.title("Создание двух одинаковых курьеров")
    @allure.description("Проверка, что нельзя создать двух курьеров с одинаковыми данными")
    def test_create_courier_duplicate(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        response = CourierAPI.create_courier(login, password, first_name)
        assert response.status_code == ResponseCode.CONFLICT
        assert response.json()["message"] == ErrorMessages.COURIER_ALREADY_EXISTS

    @allure.title("Создание курьера без поля login")
    @allure.description("Проверяем, что без поля login возвращается ошибка 400")
    def test_create_courier_missing_login(self):        
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierAPI.create_courier(None, password, first_name)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.MISSING_FIELD

    @allure.title("Создание курьера без поля password")
    @allure.description("Проверка, что без поля password возвращается ошибка 400")
    def test_create_courier_missing_password(self):     
        login = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierAPI.create_courier(login, None, first_name)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.MISSING_FIELD

    @allure.title("Создание курьера без поля firstName")
    @allure.description("Проверка, что firstName — необязательное поле, создание проходит успешно")
    def test_create_courier_missing_firstname(self):    
        login = generate_random_string(10)
        password = generate_random_string(10)
        response = CourierAPI.create_courier(login, password, None)
        assert response.status_code == ResponseCode.CREATED
        assert response.json() == {"ok": True}

    @allure.title("Создание курьера с пустым логином")
    @allure.description("Проверяем, что с пустым логином возвращается ошибка 400")
    def test_create_courier_empty_login(self):          
        # login пустой
        login = ""
        password = generate_random_string(10)
        response = CourierAPI.create_courier(login, password)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.MISSING_FIELD

    @allure.title("Создание курьера с пустым паролем")
    @allure.description("Проверка, что с пустым паролем возвращается ошибка 400")
    def test_create_courier_empty_password(self):       
        login = generate_random_string(10)
        password = ""
        response = CourierAPI.create_courier(login, password)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.MISSING_FIELD

    @allure.title("Создание курьера с уже существующим логином")
    @allure.description("Проверка, что при создании с уже существующим логином возвращается ошибка 409")
    def test_create_courier_existing_login(self):       
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        new_password = "new_password_123"
        new_first_name = "NewName"
        response = CourierAPI.create_courier(login, new_password, new_first_name)
        assert response.status_code == ResponseCode.CONFLICT
        assert response.json()["message"] == ErrorMessages.COURIER_ALREADY_EXISTS

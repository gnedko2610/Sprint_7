from constants import ResponseCode, ErrorMessages
from helpers.helpers import generate_random_string
from api.courier_api import CourierAPI
import allure


@allure.epic("Тестирование API курьера")
@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.title("Успешный логин курьера")
    @allure.description("Проверка, что курьер может авторизоваться с правильными логином и паролем")
    def test_login_courier_success(self, create_and_delete_courier):
        login = create_and_delete_courier["login"]
        password = create_and_delete_courier["password"]        
        response = CourierAPI.login_courier(login, password) 
        assert response.status_code == ResponseCode.OK
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Логин курьера без поля login")
    @allure.description("Проверка, что без поля login возвращается ошибка 400")
    def test_login_courier_missing_login(self, create_and_delete_courier):
        password = create_and_delete_courier["password"]
        response = CourierAPI.login_courier("", password)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN

    @allure.title("Логин курьера без поля password")
    @allure.description("Проверка, что без поля password возвращается ошибка 400")
    def test_login_courier_missing_password(self, create_and_delete_courier):      
        login = create_and_delete_courier["login"]
        response = CourierAPI.login_courier(login, "") 
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN

    @allure.title("Логин курьера с неправильным логином")
    @allure.description("Проверка, что при неверном логине возвращается ошибка 404")
    def test_login_courier_wrong_login(self, create_and_delete_courier):           
        password = create_and_delete_courier["password"]
        response = CourierAPI.login_courier("1", password)
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.COURIER_NOT_FOUND

    @allure.title("Логин курьера с неправильным паролем")
    @allure.description("Проверка, что при неверном пароле возвращается ошибка 404")
    def test_login_courier_wrong_password(self, create_and_delete_courier):        
        login = create_and_delete_courier["login"]
        response = CourierAPI.login_courier(login, "1")
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.COURIER_NOT_FOUND

    @allure.title("Логин несуществующего пользователя")
    @allure.description("Проверяем, что при логине несуществующего курьера возвращается ошибка 404")
    def test_login_courier_nonexistent(self):           
        login = generate_random_string(10)
        password = generate_random_string(10)
        response = CourierAPI.login_courier(login, password)
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.COURIER_NOT_FOUND

    @allure.title("Успешный логин возвращает id курьера")
    @allure.description("Проверка, что при успешной авторизации в ответе возвращается id курьера")
    def test_login_courier_returns_id(self, create_and_delete_courier):
        login = create_and_delete_courier["login"]
        password = create_and_delete_courier["password"]        
        response = CourierAPI.login_courier(login, password)             
        assert response.status_code == ResponseCode.OK
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

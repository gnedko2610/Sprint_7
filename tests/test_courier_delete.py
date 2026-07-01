from constants import ResponseCode, ErrorMessages
from helpers.helpers import generate_random_string
from api.courier_api import CourierAPI
import allure


@allure.epic("Тестирование API курьера")
@allure.feature("Удаление курьера")
class TestCourierDelete:

    @allure.title("Успешное удаление курьера")
    @allure.description("Проверка, что курьера можно удалить по id, возвращается {'ok': true}")
    def test_delete_courier_success(self):               
        login = generate_random_string(10)
        password = generate_random_string(10)
        create_response = CourierAPI.create_courier(login, password)
        login_response = CourierAPI.login_courier(login, password)
        courier_id = login_response.json()["id"]
        response = CourierAPI.delete_courier(courier_id)
        assert response.status_code == ResponseCode.OK
        assert response.json() == {"ok": True}

    @allure.title("Удаление курьера без id")
    @allure.description("Проверка, что запрос на удаление без id возвращает ошибку")
    def test_delete_courier_without_id(self):
        response = CourierAPI.delete_courier("")
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_DELETE

    @allure.title("Удаление курьера с несуществующим id")
    @allure.description("Проверка, что запрос с неверным id возвращает ошибку")
    def test_delete_courier_invalid_id(self):            
        response = CourierAPI.delete_courier(999999)
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.COURIER_ID_NOT_FOUND

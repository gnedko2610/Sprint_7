from constants import ResponseCode, ErrorMessages
from api.order_api import OrderAPI
import allure


@allure.epic("Тестирование API заказов")
@allure.feature("Получение заказа по треку")
class TestOrderGet:

    @allure.title("Успешное получение заказа по треку")
    @allure.description("Проверка, что по track можно получить данные заказа")
    def test_get_order_by_track_success(self, create_order):
        track = create_order
        response = OrderAPI.get_order_by_track(track)
        assert response.status_code == ResponseCode.OK
        assert "order" in response.json()
        assert isinstance(response.json()["order"], dict)

    @allure.title("Получение заказа без номера трека")
    @allure.description("Проверка, что запрос без track возвращает ошибку")
    def test_get_order_without_track(self):
        response = OrderAPI.get_order_by_track(None)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_SEARCH

    @allure.title("Получение заказа с несуществующим треком")
    @allure.description("Проверка, что запрос с неверным track возвращает ошибку")
    def test_get_order_invalid_track(self):
        invalid_track = 999999999
        response = OrderAPI.get_order_by_track(invalid_track)
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.ORDER_NOT_FOUND

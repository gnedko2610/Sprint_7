from constants import ResponseCode, ErrorMessages
from api.order_api import OrderAPI
import allure


@allure.epic("Тестирование API заказов")
@allure.feature("Принятие заказа")
class TestOrderAccept:

    @allure.title("Успешное принятие заказа курьером")
    @allure.description("Проверка, что курьер может принять заказ, возвращается {'ok': true}")
    def test_accept_order_success(self, create_and_delete_courier, create_order):
        courier_id = create_and_delete_courier["id"]
        track = create_order
        order_response = OrderAPI.get_order_by_track(track)
        order_id = order_response.json()["order"]["id"]
        response = OrderAPI.accept_order(order_id, courier_id)
        assert response.status_code == ResponseCode.OK
        assert response.json() == {"ok": True}

    @allure.title("Принятие заказа без id курьера")
    @allure.description("Проверка, что запрос без courierId возвращает ошибку")
    def test_accept_order_without_courier_id(self, create_order):
        track = create_order
        order_response = OrderAPI.get_order_by_track(track)
        order_id = order_response.json()["order"]["id"]
        response = OrderAPI.accept_order(order_id, None)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_SEARCH

    @allure.title("Принятие заказа с неверным id курьера")
    @allure.description("Проверка, что запрос с несуществующим courierId возвращает ошибку")
    def test_accept_order_invalid_courier_id(self, create_order):
        track = create_order
        order_response = OrderAPI.get_order_by_track(track)
        order_id = order_response.json()["order"]["id"]
        response = OrderAPI.accept_order(order_id, 999999)
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.COURIER_ID_NOT_EXISTS

    @allure.title("Принятие заказа без id заказа")
    @allure.description("Проверка, что запрос без orderId возвращает ошибку")
    def test_accept_order_without_order_id(self, create_and_delete_courier):
        courier_id = create_and_delete_courier["id"]
        response = OrderAPI.accept_order("", courier_id)
        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_SEARCH

    @allure.title("Принятие заказа с неверным id заказа")
    @allure.description("Проверка, что запрос с несуществующим orderId возвращает ошибку")
    def test_accept_order_invalid_order_id(self, create_and_delete_courier):
        courier_id = create_and_delete_courier["id"]
        response = OrderAPI.accept_order(999999, courier_id)
        assert response.status_code == ResponseCode.NOT_FOUND
        assert response.json()["message"] == ErrorMessages.ORDER_ID_NOT_EXISTS

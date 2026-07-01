from constants import ResponseCode
from api.order_api import OrderAPI
import allure


@allure.epic("Тестирование API заказов")
@allure.feature("Список заказов")
class TestOrderList:    

    @allure.title("Получение списка заказов")
    @allure.description("Проверка, что запрос возвращает список заказов")
    def test_get_orders_list(self):
        response = OrderAPI.get_orders()
        assert response.status_code == ResponseCode.OK
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

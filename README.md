api/                        
    courier_api.py - методы для курьеров
    order_api.py - методы для заказов
data/
    test_data.py - тестовые данные для параметризации
helpers/
    helpers.py - генерация данных, вспомогательные функции
tests/
    test_courier_create.py - тесты на создание курьера
    test_courier_login.py - тесты на логин курьера
    test_order_create.py - тесты на создание заказа
    test_order_list.py - тесты на список заказов
    test_courier_delete.py - доп. тесты на удаление курьера
    test_order_accept.py - доп. тесты на принятие заказа
    test_order_get.py - доп. тесты на получение заказа по номеру
conftest.py - фикстуры
constants.py - константы (URL, эндпоинты)
.gitignore
README.md

Для запуска тестов должны быть установлены:
requests, pytest, allure

Команда для запуска тестов:
pytest -v

Команда для генерации Allure-отчёта:
pytest --alluredir=allure_results

Команда для формирования отчёта в формате веб-страницы:
allure serve allure_results
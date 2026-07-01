class URL:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

class Endpoints:
    COURIER = "/api/v1/courier"
    LOGIN = "/api/v1/courier/login"
    ORDERS = "/api/v1/orders"
    ORDER_ACCEPT = "/api/v1/orders/accept"
    ORDER_TRACK = "/api/v1/orders/track"

class ResponseCode:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409

class ErrorMessages:
    COURIER_ALREADY_EXISTS = "Этот логин уже используется. Попробуйте другой."
    MISSING_FIELD = "Недостаточно данных для создания учетной записи"
    INSUFFICIENT_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    COURIER_NOT_FOUND = "Учетная запись не найдена"
    INSUFFICIENT_DATA_FOR_DELETE = "Недостаточно данных для удаления курьера"
    COURIER_ID_NOT_FOUND = "Курьера с таким id нет."
    ORDER_NOT_FOUND = "Заказ не найден"
    INSUFFICIENT_DATA_FOR_SEARCH = "Недостаточно данных для поиска"
    COURIER_ID_NOT_EXISTS = "Курьера с таким id не существует"
    ORDER_ID_NOT_EXISTS = "Заказа с таким id не существует"

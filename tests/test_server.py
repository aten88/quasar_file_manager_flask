from http import HTTPStatus

import requests

from app.main.quasar_junior_flask_server import (
    allowed_ext_file,
    ALLOWED_EXTENSIONS
)

from configuration import (
    INDEX_URL,
    GET_URL,
    TEST_EXTENSIONS,
    TEST_URL_FILENAMES
)


def test_extension():
    """ Тест проверки расширения файлов. """
    extensions = '.txt', '.csv', '.json', '.xlsx', '.jpg', '.png'
    for extension in extensions:
        assert allowed_ext_file(extension) is True, 'Ошибка в расширении файла'


def test_index():
    response = requests.get(url=INDEX_URL)
    assert response.status_code == HTTPStatus.OK, 'Ошибка сетевого запроса'


def test_request_list_files():
    response = requests.get(url=GET_URL + '/list')
    recieved_data = response.json()
    print(recieved_data)
    assert response.status_code == HTTPStatus.OK, 'Ошибка сетевого запроса'
    assert isinstance(recieved_data, list) is True, (
        'Тип полученных данных не является списком'
    )


def test_request_extension():
    for extention in TEST_EXTENSIONS:
        response = requests.get(url=GET_URL+extention)
        assert response.status_code == HTTPStatus.OK, 'Ошибка расширения в URL'
        assert (extention in ALLOWED_EXTENSIONS) is True, (
            'Переданное расширение не соответствует списку разрешенных'
        )


def test_request_extension_file():
    for file in TEST_URL_FILENAMES:
        response = requests.get(url=GET_URL + file)
        assert response.status_code == HTTPStatus.OK, (
            'Ошибка имени файла в URL'
        )
# assert Проверка файла в хранилище


# def test_create_file():
#     response = requests.get(url='http://127.0.0.1:4567/files/create')
#     assert response.status_code == HTTPStatus.OK

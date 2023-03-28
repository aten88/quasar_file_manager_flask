from http import HTTPStatus

import requests

from app.main.quasar_junior_flask_server import (
    allowed_ext_file,
    ALLOWED_EXTENSIONS
)

from configuration import (
    INDEX_URL,
    LIST_URL,
    TYPE_URL,
    TEST_EXTENSIONS,
    TEST_FILENAMES
)


def test_extension():
    """ Тест проверки расширения файлов. """
    extensions = '.txt', '.csv', '.json', '.xlsx', '.jpg', '.png'
    for extension in extensions:
        assert allowed_ext_file(extension) is True, 'Ошибка в расширении файла'


def test_index():
    response = requests.get(url=INDEX_URL)
    assert response.status_code == HTTPStatus.OK, 'Ошибка сетевого запроса'
    # assert redirect


def test_request_data_type():
    response = requests.get(url=LIST_URL)
    recieved_data = response.json()

    assert response.status_code == HTTPStatus.OK, 'Ошибка сетевого запроса'
    assert type(recieved_data) == list, (
        'Тип полученных данных не является списком'
    )


def test_request_extension():
    for extention in TEST_EXTENSIONS:
        response = requests.get(url=TYPE_URL+extention)
        assert response.status_code == HTTPStatus.OK, 'Ошибка расширения в URL'
        assert (extention in ALLOWED_EXTENSIONS) is True, (
            'Переданное расширение не соответствует списку разрешенных'
        )


def test_request_extension_file():
    for file in TEST_FILENAMES:
        response = requests.get(url=TYPE_URL + file)
        assert response.status_code == HTTPStatus.OK, (
            'Ошибка имени файла в URL'
        )
# assert Проверка файла в хранилище

from http import HTTPStatus

import requests

from app.main.quasar_junior_flask_server import (
    allowed_ext_file,
    get_type_files
)

from configuration import INDEX_URL, LIST_URL, TYPE_URL
from constants import ALLOWED_EXTENSIONS


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
    extensions = 'txt', 'csv', 'json', 'xlsx', 'jpg', 'png'
    for extention in extensions:
        response = requests.get(url=TYPE_URL+extention)
        assert response.status_code == HTTPStatus.OK, 'Ошибка расширения в URL'
    assert (extention in ALLOWED_EXTENSIONS) is True, (
        'Переданное расширение не соответствует списку разрешенных'
    )

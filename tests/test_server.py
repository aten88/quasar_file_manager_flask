import io

from http import HTTPStatus
from flask.testing import FlaskClient

from app.main.quasar_junior_flask_server import (
    allowed_ext_file,
    ALLOWED_EXTENSIONS
)

from configuration import (
    GET_URL,
    TEST_EXTENSIONS,
    WRONG_TEST_EXTENSIONS
)


def test_extension():
    """ Check extensions test. """
    for extension in TEST_EXTENSIONS:
        assert allowed_ext_file(f'.{extension}') is True, (
            'Ошибка в расширении файла'
        )


def test_file_list(client: FlaskClient):
    """ Test get files list """
    response = client.get(f'{GET_URL}/list')
    assert response.status_code == HTTPStatus.OK, 'Ошибка расширения в URL.'
    assert isinstance(response.json, list) is True, (
        'Полученный объект не является списком.'
    )


def test_request_extension(client: FlaskClient):
    """ Test extensions is allowed. """
    for extention in TEST_EXTENSIONS:
        response = client.get(f'{GET_URL}/{extention}')
        assert response.status_code == HTTPStatus.OK, 'Ошибка расширения в URL'
        assert (extention in ALLOWED_EXTENSIONS) is True, (
            'Переданное расширение не соответствует списку разрешенных'
        )


def test_request_wrong_extension(client: FlaskClient):
    """ Test wrong extensions not allowed. """
    for extention in WRONG_TEST_EXTENSIONS:
        response = client.get(f'{GET_URL}/{extention}')
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert (extention in ALLOWED_EXTENSIONS) is False, (
            'Переданное расширение не соответствует списку разрешенных'
        )


def test_request_extension_file(client: FlaskClient):
    """ Test get file by extension. """
    response = client.get(f'{GET_URL}/jpg/Тест')
    assert response.status_code == HTTPStatus.OK, 'Ошибка в URL'
    assert response.data.decode('utf-8') == 'Тест.jpg', (
        'Не соответствие имени файла'
    )


def test_request_not_extension_file(client: FlaskClient):
    """ Test not get file by wrong extension. """
    response = client.get(f'{GET_URL}/wtf/NOTtest')
    assert response.status_code == HTTPStatus.BAD_REQUEST, 'Ошибка в URL'
    assert response.data.decode('utf-8') != 'NOTtest.wtf', (
        'Не соответствие имени файла'
    )


def test_create_file(client: FlaskClient):
    """ Test save file. """
    data = {
        'file': (io.BytesIO(b'021202202'), 'TEST_SAVED.txt')
    }
    response = client.post('/files/create', data=data)
    assert len(response.data) > 1, (
        'Ошибка сохранения файла в запросе передано больше 1 файла.'
    )
    assert response.status_code == HTTPStatus.OK, 'Ошибка сохранения файла.'


def test_delete(client: FlaskClient):
    """ Test delete file. """
    response = client.delete('/files/delete/TEST_SAVED.txt')
    assert response.status_code == HTTPStatus.OK, 'Ошибка удаления файла.'


def test_wrong_delete(client: FlaskClient):
    """ Test not delete not exist file. """
    response = client.delete('/files/delete/NOT_TEST_SAVED.txt')
    assert response.status_code == HTTPStatus.BAD_REQUEST, (
        'Ошибка теста, файл с таким именем существует.'
    )

# from http import HTTPStatus

# from flask import redirect

from app.main.quasar_junior_flask_server import allowed_ext_file


def test_extension():
    """ Тест проверки расширения файлов. """
    extensions = '.txt', '.csv', '.json', '.xlsx', '.jpg', '.png'
    for extension in extensions:
        assert allowed_ext_file(extension) is True, 'Ошибка в расширении файла'


# def test_index():
#     """ Тест проверки редиректа на страницу со списком файлов"""

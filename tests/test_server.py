from app.main.quasar_junior_flask_server import allowed_ext_file


def test_extension():
    test_file = 'Тестовый файл.txt'
    assert allowed_ext_file(test_file) is True, 'Тест не пройден'

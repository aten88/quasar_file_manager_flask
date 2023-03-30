from pathlib import Path

# Этот файл содержит в себе константы,
# которые неоднократно будут применены в коде.
# https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html?ysclid=lfuwj4uiwd75389176#section-29
GET_URL = '/files/get'
TEST_EXTENSIONS = 'txt', 'csv', 'json', 'xlsx', 'jpg', 'png'
WRONG_TEST_EXTENSIONS = 'bin', 'doc', 'pic', 'exe', 'zip', 'rar'
BASE_DIR = Path(__file__).parent
TEST_FILES_DIR = BASE_DIR.joinpath('TEST_Storage')

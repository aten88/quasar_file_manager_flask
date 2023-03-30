from pathlib import Path

# Этот файл содержит в себе константы,
# которые неоднократно будут применены в коде.
# https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html?ysclid=lfuwj4uiwd75389176#section-29
BASE_PATH = Path(__file__).parent
UPLOAD_FOLDER = BASE_PATH.joinpath('Storage')
UPLOAD_FOLDER.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {'txt', 'csv', 'json', 'xlsx', 'jpg', 'png'}
MAX_SIZE = 16 * 1024 * 1024

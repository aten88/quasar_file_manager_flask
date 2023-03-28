from pathlib import Path

BASE_PATH = Path(__file__).parent
UPLOAD_FOLDER = BASE_PATH.joinpath('Storage')
UPLOAD_FOLDER.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {'txt', 'csv', 'json', 'xlsx', 'jpg', 'png'}
MAX_SIZE = 16 * 1024 * 1024

from http import HTTPStatus

from pathlib import Path

from flask import Flask, abort, request, send_file, redirect

# from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, MAX_SIZE


app = Flask(__name__)

app.config['UPLOAD_FOLDER']: Path = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_SIZE


def allowed_ext_file(filename):
    """ Extension files check method """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    """ Main page method """
    return redirect('/files/get/list')


@app.route("/files/get/list", methods=["GET"])
def get_files_list():
    """ Get list files method """
    files = app.config['UPLOAD_FOLDER'].iterdir()
    return [
        file.name for file in files
        if file.is_file() and file.suffix[1:] in ALLOWED_EXTENSIONS
    ]


@app.route("/files/get/<string:extension>", methods=["GET"])
def get_type_files(extension):
    """ Get files by extension """
    if extension not in ALLOWED_EXTENSIONS:
        abort(HTTPStatus.BAD_REQUEST, "Расширение недопустимо!")
    files = app.config['UPLOAD_FOLDER'].glob(f'*.{extension}')
    return [file.name for file in files if file.is_file()]


@app.route("/files/get/<string:extension>/<string:file_name>", methods=["GET"])
def get_file(extension, file_name):
    """ Get files by extension and filename """
    if extension not in ALLOWED_EXTENSIONS:
        abort(HTTPStatus.BAD_REQUEST, "Расширение недопустимо!")
    file = app.config['UPLOAD_FOLDER'].joinpath(f'{file_name}.{extension}')
    if not file.exists():
        abort(HTTPStatus.BAD_REQUEST, "Файл недоступен!")
    return send_file(file)


@app.route("/files/create", methods=["POST"])
def create_file():
    """ Save file to Storage """
    files = request.files.getlist('file')
    if len(files) > 1:
        abort(HTTPStatus.BAD_REQUEST, "В запросе больше 1 файла!")
    file = files[0]
    if not allowed_ext_file(file.filename):
        abort(HTTPStatus.BAD_REQUEST, "Расширение недопустимо!")
    # TODO filename = secure_filename(file.filename) этот метод под капотом
    # не работает с кириллицей
    saved_file = app.config['UPLOAD_FOLDER'].joinpath(file.filename)
    if saved_file.exists():
        abort(HTTPStatus.BAD_REQUEST, "Файл уже существует!")
    file.save(saved_file)
    return {"message": "Файл сохранен"}


@app.route("/files/delete/<string:file_name>", methods=["DELETE"])
def delete_file(file_name):
    """ Delete file from Storage """
    file = app.config['UPLOAD_FOLDER'].joinpath(f'{file_name}')
    if not allowed_ext_file(file.name):
        abort(HTTPStatus.BAD_REQUEST, "Расширение недопустимо!")
    if not file.exists() and not file.is_file():
        abort(HTTPStatus.BAD_REQUEST, "Файл несуществует!")
    file.unlink()
    return f"Файл {file_name} удален."


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4567)

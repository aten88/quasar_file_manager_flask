import os

from flask import Flask

app = Flask(__name__)


@app.route("/files/get/list")
def get_files():
    path = "C:\Dev\Quasar\Quasar_test_junior_FLASK\Storage"
    dir_list = os.listdir(path)
    return dir_list


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

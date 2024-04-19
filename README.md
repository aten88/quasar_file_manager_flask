# Файловый API-менеджер для компании Quasar
## Функционал проекта: 
- создавать, редактировать и загружать файлы допустимых расширений с и использованием API интерфейса.
#### Стек проекта: Python 3.11, Flask 2.2.3, Jinja2 3.1.2, requests 2.28.2, pytest 7.2.2
## Как запустить проект:
  - Клонировать репозиторий и перейти в него в командной строке:
    ```
    git clone git@github.com:aten88/quasar_file_manager_flask.git
    ```
    ```
    cd quasar_file_manager_flask
    ```
  - Cоздать и активировать виртуальное окружение установить Python 3.11:
    ```
    py -3.11 -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
  - Обновить pip:
    ```
    python -m pip install --upgrade pip
    ```
  - Установить зависимости из файла requirements.txt:
    ```
    pip install -r requirements.txt
    ```
  - Запустить исполняемый файл:
    ```
    quasar_server.py
    ```
  - Сделать запрос к эндпоинтам API:
    ```
    /files/get/list
    /files/get/<string:extension>
    /files/get/<string:extension>/<string:file_name>
    /files/create
    /files/delete/<string:file_name>
    ```
### Автор Алексей Тен

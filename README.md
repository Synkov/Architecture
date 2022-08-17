# Запуск фреймворка с помощью uwsgi:

1.Установка библиотеки uwsgi:
    pip install uwsgi
2. Запуск:
    uwsgi --http :8000 --wsgi-file main.py
# Architecture_and_design_patterns_in_Python
Приложение создано с использованием виртуального окружения

virtualenv venv --python=python3.9

Активация виртуального окружения

source venv/bin/activate

Установка зависимостей

pip install -r requirements.txt

Запуск приложения с использованием Gunicorn

gunicorn -w 4 app.main:application --bind 127.0.0.1:8080


Название фреймворка Cat, который вынесен в отдельный каталог. Приложение находитсяя в каталоге app.
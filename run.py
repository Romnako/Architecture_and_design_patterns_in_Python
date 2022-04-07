from wsgiref.simple_server import make_server
from cat.core import Cat
from app.urlpatterns import urlpatterns, front_controllers

application = Cat(urlpatterns, front_controllers)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
from cat.core import Cat
from app.urlpatterns import urlpatterns, front_controllers
from quopri import decodestring



application = Cat(urlpatterns, front_controllers)


def decode_value(data):
        new_data = {}
        for k, v in data.items():
            key = bytes(k.replace('%', '=').replace("+", " "), 'UTF-8')
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            key_decode_str = decodestring(key).decode('UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

if __name__ == '__main__':
    application.run()
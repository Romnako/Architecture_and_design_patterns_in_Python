from cat import Cat
from .urlpatterns import urlpatterns, front_controllers


application = Cat(urlpatterns, front_controllers)

if __name__ == '__main__':
    application.run()
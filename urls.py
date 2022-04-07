from datetime import date
from views import Index, About, CreateCategory, CategoriesList, Contact, CopyCourse, CreateCourse, CoursesList, Learning


routes ={
    '/': Index(),
    '/about/': About(),
    '/categories/create': CreateCategory(),
    '/categories': CategoriesList(),
    '/contact': Contact(),
    '/courses/copy': CopyCourse(),
    '/courses/create': CreateCourse(),
    '/courses': CoursesList(),
    '/learning': Learning(),
}
# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

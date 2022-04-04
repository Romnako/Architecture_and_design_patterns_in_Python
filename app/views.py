from cat import render
from patterns.creational_patterns import Logger, Engine
from pprint import pprint

class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', page='index')

class About:
    def __call__(self, request):
        return '200 OK', render('about.html', page='about')

class Learning:
    def __call__(self, request):
        promocode = request.get('promocode', None)
        date = request.get('date', None)
        cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург']
        courses = [
            {
                'title': 'Основы Python',
                'schedule': [
                    {
                        'date': 'Вс, 20 февраля 2022',
                        'time': '11:00 - 14:00'
                    },
                    {
                        'date': 'Вс, 6 марта 2022',
                        'time': '11:00 - 14:00'
                    },
                    {
                        'date': 'Вс, 20 марта 2022',
                        'time': '11:00 - 14:00'
                    },
                ]
            },
            {
                'title': 'Алгоритмы и структуры данных на Python',
                'schedule': [
                    {
                        'date': 'Вс, 10 апреля 2022',
                        'time': '11:00 - 13:00'
                    },
                    {
                        'date': 'Вс, 1 мая 2022',
                        'time': '11:00 - 13:00'
                    },
                    {
                        'date': 'Вс, 8 мая 2022',
                        'time': '11:00 - 13:00'
                    },
                ]
            },
            {
                'title': 'Основы Django',
                'schedule': [
                    {
                        'date': 'Вс, 26 июня 2022',
                        'time': '11:00 - 13:00'
                    },
                    {
                        'date': 'Вс, 3 июля 2022',
                        'time': '11:00 - 13:00'
                    },
                    {
                        'date': 'Вс, 10 июля 2022',
                        'time': '11:00 - 13:00'
                    },
                ]
            },
            {
                'title': 'Основы Flask',
                'schedule': [
                    {
                        'date': 'Вс, 28 августа 2022',
                        'time': '11:00 - 16:00'
                    },
                    {
                        'date': 'Вс, 4 сентября 2022',
                        'time': '11:00 - 16:00'
                    },
                    {
                        'date': 'Вс, 11 сентября 2022',
                        'time': '11:00 - 16:00'
                    },
                ]
            }
        ]
        return '200 OK', render('learning.html', date=date, cities=cities, courses=courses, promocode=promocode, page='learning')


class Contact:
    def __call__(self, request):
        if 'params' in request and request['method'] == 'POST':
            contact = ', '.join("{!s}={!r}".format(key, val) for (key, val) in request['params'].items())
            with open("contacts.txt", "a+") as contacts_file:
                contacts_file.write(contact + "\n")

        return '200 OK', render('contact.html', page='contact')


class CreateCategory:
    def __call__(self, request):
        Logger.log('LogLine: ' + str(request.get('date').strftime('%H:%M:%S')) + ' - создание категории!')
        if request['method'] == 'POST':
            name = request['params'].get('name', None)

            # TODO: Session postback
            if Engine.get_category_by_name(name) is not None:
                raise Exception('Категория с таким именем уже создана!')

            category = Engine.create_category(name)
            Engine.categories.append(category)

            pprint(vars(category))
            pprint([Engine.categories])

            return '200 OK', render('categories.html', categories_list=Engine.categories, page='categories')
        else:
            return '200 OK', render('category_create.html', page='category_create')


class CategoriesList:
    def __call__(self, request):
        Logger.log('LogLine: ' + str(request.get('date').strftime('%H:%M:%S')) + ' - список категорий')
        return '200 OK', render('categories.html', categories_list=Engine.categories, page='categories')


class CreateCourse:
    category_id = 0

    def __call__(self, request):
        Logger.log('LogLine: ' + str(request.get('date').strftime('%H:%M:%S')) + ' - создание курса!')
        if request['method'] == 'POST':
            name = request['params'].get('name', None)
            type_alias = request['params'].get('type_alias', None)

            # TODO: Session postback
            if not name:
                raise Exception('Необходимо указать название курса!')

            if type_alias not in ['webinar', 'interactive', 'video']:
                raise Exception('Некорректный тип курса!')

            category = None
            if self.category_id != 0:
                category = Engine.get_category_by_id(int(self.category_id))

                course = Engine.create_course(type_alias, name, category)
                Engine.courses.append(course)

            return '200 OK', render('courses.html', courses_list=Engine.courses)

        else:
            try:
                self.category_id = request['params'].get('id')
                category = Engine.get_category_by_id(int(self.category_id))

                return '200 OK', render('course_create.html', category=category)
            except KeyError:
                return '200 OK', 'Сначала нужно добавить категории!'


class CoursesList:
    def __call__(self, request):
        Logger.log('LogLine: ' + str(request.get('date').strftime('%H:%M:%S')) + ' - список курсов!')
        try:
            category = Engine.get_category_by_id(request['params'].get('id'))
            return '200 OK', render('courses.html', courses_list=category.courses, page='courses')

        except KeyError:
            return '200 OK', 'Список курсов пуст!'


class CopyCourse:
    def __call__(self, request):
        Logger.log('LogLine: ' + str(request.get('date').strftime('%H:%M:%S')) + ' - копирование курса!')

        try:
            name = request['params'].get('name', None)

            if not name:
                raise Exception('Не указано название курса, который будет скопирован!')

            copied_course = Engine.get_course_by_name(name)

            if not copied_course:
                raise Exception('Курс с таким именем не найден!')

            if copied_course:
                new_name = f'copy_{name}'
                course = copied_course.clone()
                course.name = new_name
                Engine.courses.append(course)

            return '200 OK', render('courses.html', courses_list=Engine.courses)

        except KeyError:
            return '200 OK', 'Список курсов пуст!'

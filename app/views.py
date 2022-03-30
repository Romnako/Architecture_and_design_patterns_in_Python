from cat import render


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
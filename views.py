from cat.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', About()


class CreateCategory:
    def __call__(self):
        return '200 OK', CreateCategory()


class CategoriesList:
    def __call__(self):
        return '200 OK', CategoriesList()


class Contact:
    def __call__(self):
        return '200 OK', Contact()


class CopyCourse:
    def __call__(self):
        return '200 OK', CopyCourse()


class CreateCourse:
    def __call__(self):
        return '200 OK', CreateCourse()


class CoursesList:
    def __call__(self):
        return '200 OK', CoursesList()


class Learning:
    def __call__(self):
        return '200 OK', Learning()
from home_framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', 'about'


class Contacts:
    def __call__(self):
        return '200 OK', '<h1>contacts</h1>'

class PageNotFoubd404:
    def __call__(self):
        return PageNotFoubd404()
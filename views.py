from home_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class About:
    def __call__(self, request):
        return '200 OK', 'about'


class PageNotFoubd404:
    def __call__(self, requests):
        return PageNotFoubd404()
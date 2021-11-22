from thesand_framework.templator import render


# page controller
class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get('data', None))


class Something:
    def __call__(self, request):
        return '200 OK', render('something.html', data=request.get('data', None))

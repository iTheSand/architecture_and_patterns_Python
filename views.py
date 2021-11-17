from thesand_framework.templator import render


# page controller
class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class Contacts:
    def __call__(self):
        return '200 OK', render('contacts.html')

from views import Index, Contacts, Something
from datetime import date


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/contacts/': Contacts(),
    '/something/': Something()
}

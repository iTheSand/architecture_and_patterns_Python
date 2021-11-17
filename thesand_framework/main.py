class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 PAGE Not Found'


class Application:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

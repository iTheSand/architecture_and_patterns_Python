from thesand_framework.main import Application
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = Application(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()

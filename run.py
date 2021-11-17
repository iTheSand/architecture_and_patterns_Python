from wsgiref.simple_server import make_server
from thesand_framework.main import Application
from urls import routes

application = Application(routes)

with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()

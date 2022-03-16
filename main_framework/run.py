from wsgiref.simple_server import make_server
from thesand_framework.main import Framework, FakeFramework
from urls import fronts
from views import routes

application = Framework(routes, fronts)
# application = FakeFramework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()

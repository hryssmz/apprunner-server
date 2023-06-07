import os
from typing import Any
from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request: Any) -> Response:
    name = os.environ.get("NAME", None)
    if name is None or len(name) == 0:
        name = "world"
    message = "Good morning, " + name + "!\n"
    return Response(message)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "80"))
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_view(hello_world, route_name="hello")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", port, app)
    server.serve_forever()

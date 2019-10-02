from server.base_http_server import BaseHTTPServer


class SimpleHTTPServer(BaseHTTPServer):
    def __init__(self, server_address, handler_class):
        BaseHTTPServer.__init__(self, server_address, handler_class)

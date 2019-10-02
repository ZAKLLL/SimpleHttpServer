from server.socket_server import TcpServer


class BaseHTTPServer(TcpServer):
    def __init__(self, server_address, handler_class):
        TcpServer.__init__(self, server_address, handler_class)


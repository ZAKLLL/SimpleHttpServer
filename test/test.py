import socket
import threading

from handler.base_handler import StreamRequestHandler
from server.socket_server import TcpServer
from server.base_http_server import BaseHTTPServer
from handler.base_http_handler import BaseHTTPRequestHandler


class TestBaseRequestHandler(StreamRequestHandler):

    # 具体处理逻辑
    def handle(self):
        msg = self.readline()
        print('Server recv msg:' + msg)
        self.write_content(msg)
        self.send()
        pass


class SocketServerTest:

    def run_server(self):
        tcp_server = TcpServer(('127.0.0.1', 8080), TestBaseRequestHandler)
        tcp_server.server_forever()

    def gen_client(self, num):
        print("开始生产客户端")
        clients = []
        for i in range(num):
            # todo 实现客户端的具体链接逻辑
            client_thread = threading.Thread(target=self.client_connet)
            clients.append(client_thread)
        return clients

    def client_connet(self):
        client = socket.socket()
        client.connect(('127.0.0.1', 8080))
        client.send(b'Hello TcpServer\r\n')
        msg = client.recv(1024)
        print('Client recv msg:' + msg.decode())

    def run(self):

        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        clients = self.gen_client(5)
        for client in clients:
            client.start()
            client.join()

        server_thread.join()


class BaseHTTPRequestHandlerTEST:

    def run_server(self):
        BaseHTTPServer(('127.0.0.1', 8080), BaseHTTPRequestHandler).server_forever()

    def run(self):
        self.run_server()


from server.simple_http_server import SimpleHTTPServer
from handler.simple_http_handler import SimpleHTTPRequestHandler


class SimpleHTTPRequestHandlerTest:
    def run(self):
        SimpleHTTPServer(('127.0.0.1', 8080), SimpleHTTPRequestHandler).server_forever()


if __name__ == '__main__':
    # SocketServerTest().run()
    # BaseHTTPRequestHandlerTEST().run()
    SimpleHTTPRequestHandlerTest().run()

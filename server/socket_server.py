# _*_encoding=utf-8 _*_

import socket
import threading


class TcpServer:
    def __init__(self, server_address, Handler_class):
        self.server_address = server_address
        self.HandlerClass = Handler_class
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_shutdown = False

    # 服务器启动函数
    def server_forever(self):
        self.socket.bind(self.server_address)
        self.socket.listen(10)
        while not self.is_shutdown:
            # 接受请求
            request, client_address = self.socket.accept()
            # 处理请求
            try:
                self.process_request_multithread(request, client_address)
            except Exception as e:
                print(e)


    # 接受请求
    def get_request(self):
        return self.socket.accept()

    # 处理请求
    def process_request(self, request, addr):
        handler = self.HandlerClass(self, request, addr)
        handler.handle()
        self.close_request(request)

    # 多线程处理请求
    def process_request_multithread(self, request, addr):
        t = threading.Thread(target=self.process_request, args=(request, addr))
        t.start()

    # 关闭请求
    def close_request(self, request):
        request.shutdown(socket.SHUT_WR)
        request.close()
        pass

    # 关闭服务器
    def shutdown(self):
        self.is_shutdown = True

        pass

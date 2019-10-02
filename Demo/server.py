import socket


def server():
    # 创建套接字
    s = socket.socket()
    # 绑定套接字
    HOST = '127.0.0.1'
    PORT = 6666
    s.bind((HOST, PORT))
    # 监听
    s.listen(5)

    while True:
        c, addr = s.accept()
        print('Connect client:', addr)
        msg = c.recv(1024)
        c.send(msg)

    pass


if __name__ == "__main__":
    server()

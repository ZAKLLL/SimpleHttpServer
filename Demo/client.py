# _*_encoding=utf-8 _*_

import socket


def client():
    s = socket.socket()

    HOST = '127.0.0.1'
    PORT = 6666
    s.connect((HOST, PORT))
    s.send(b"Hello,World ")
    msg = s.recv(1024)
    print("Print From Server:", msg)


if __name__ == "__main__":
    client()

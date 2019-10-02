import os
import json
from handler.base_http_handler import BaseHTTPRequestHandler
from urllib import parse

RESOURCES_PATH = os.path.join(os.path.abspath(os.path.dirname(__name__)),
                              '../resources')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, server, request, client_address):
        BaseHTTPRequestHandler.__init__(self, server, request, client_address)

    # 处理Get请求
    def do_GET(self):
        is_found, resource_path = self.get_resources(self.path)
        if not is_found:
            self.write_error(404)
        else:
            with open(resource_path, 'rb') as f:
                fs = os.fstat(f.fileno())
                # 获取文件长度
                f_length = fs[6]
                self.write_response(200, None)
                self.write_header('Content-length', f_length)
                # 避免跨域问题
                self.write_header('Access-Control-Allow-Origin',
                                  'http://%s:%d' %
                                  (self.server.server_address[0], self.server.server_address[1]))
                # 结束应答头编写
                self.end_headers()

                # 开始写入数据到应答内容中
                while True:
                    buf = f.read(1024)
                    if not buf:
                        break
                    self.write_content(buf)

    def do_POST(self):
        pass

    # 判断并且获取资源
    def get_resources(self, path):
        url_request = parse.urlparse(path)
        # 该函数返回值为(scheme='', netloc='', path='/index.html', params='', query='a=1', fragment='')
        # 取第三个参数作为资源路径
        resource_path = str(url_request[2])
        if resource_path.startswith('/'):
            # 去除斜杠
            resource_path = resource_path[1:]
        resource_path = os.path.join(RESOURCES_PATH, resource_path)
        # 判断该文件路径是否存在
        if os.path.exists(resource_path) and os.path.isfile(resource_path):
            return True, resource_path
        else:
            return False, resource_path

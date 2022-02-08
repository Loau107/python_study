'''
静态 web 服务端
'''
import socket
import threading
import sys


class WebServer:
    def __init__(self, port = 8080):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server_socket.bind(('', port))
        self.tcp_server_socket.listen(128)

    def start(self):
        while True:
            client_socket, client_addr = self.tcp_server_socket.accept()
            sub_handler_client = threading.Thread(target=self.handler_client, args=((client_socket,)), daemon=True)
            sub_handler_client.start()
            # self.handler_clzient(client_socket)


    @staticmethod
    def handler_client(client_socket):
        recv_data = client_socket.recv(100000).decode()

        # 检测客户端是否退出
        if len(recv_data) == 0:
            client_socket.close()
            return

        # 读取路径信息
        path = recv_data.split(' ')[1]

        # 设置主页
        if path == '/':
            path = '/index.html'

        print('客户端请求 :', path[1 : len(path)])

        # 读取文件资源
        try:
            print('path =', path)
            f = open('file' + path, 'rb')
            file_data = f.read()
            f.close()
        except Exception as e:
            print('\n--客户端输入了错误的路径\n')
            # 响应报文
            response_line = 'HTTP/1.1 404 NOT FOUND\r\n'
            response_head = ''
            response_body = '404 NOT FOUND'
            response_data = (response_line + response_head + '\r\n' + response_body).encode()
            # 发送资源
            client_socket.send(response_data)
            client_socket.close()
        else:
            # 响应报文
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_head = ''
            response_body = file_data
            response_data = (response_line + response_head + '\r\n').encode() + response_body
            # 发送资源
            client_socket.send(response_data)
            client_socket.close()


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # 获取获取终端写入的端口号
    except:
        web_server = WebServer()
    else:
        web_server = WebServer(port)

    web_server.start()
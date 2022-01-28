# 客户端
'''
# 步骤：1、创建 socket 2、与服务端建立连接 3、发送接收数据 4、释放资源

# 1、创建客户端套接字对象（socket）
import socket
# 参数 1：IP 协议的版本 socket.AF_INET == 'IPV4'
# 参数 2：通信协议 socket.SOCK_STREAM == 'TCP协议'
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、与服务器套接字建立连接
# 参数：有两个元素的元组（是只有一个元组参数，元组里面拥有两个元素，而不是函数有两个参数）
# 元素 1：服务器的 IP 地址
# 元素 2：服务器的端口号
tcp_client_socket.connect(('192.168.0.198', 8080))

# 3、发送数据
str = input('输入消息：\n')
tcp_client_socket.send(str.encode('utf-8'))

# 4、收发数据
recv_data = tcp_client_socket.recv(1024) # 参数是以字节为单位的数据大小
print('\n接收回复：')
print(recv_data.decode('utf-8'))

# 5、关闭客户端套接字
tcp_client_socket.close()
'''

# 组合多线程的小案例
'''
import socket
import threading

t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(('192.168.0.190', 8080))

mutex = threading.Lock()

def recv():
    while True:
        print('接收消息：\n', t.recv(1024).decode('utf-8'))

if __name__ == '__main__':
    p_recv = threading.Thread(target=recv, daemon=True)
    p_recv.start()
    while True:
        st = input() + '\n'
        if st == '0\n':
            t.close()
            exit()
        else:
            t.send(st.encode('utf-8'))
'''


# 服务端
# 1、创建服务端端套接字对象
import socket
# 参数 1：ipv4  参数 2：tcp协议
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口复用
# 端口复用，让程序在退出时端口号自动释放
# setsockopt：设置 socket 选项
# SOL_SOCKET：socket 选项列表   SO——REUSEADDR：地址复用   True：开启此选项
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 2、绑定端口号
# 参数：元组（两个参数）  元素 1：IP 地址  元素 2：端口号
# 参数 1 默认为本机的 IP 地址  也可以直接写 127.0.0.1
tcp_server_socket.bind(('127.0.0.1', 8080))

# 3、设置监听
# 参数：最大监听个数（能同时监听的客户端个数）
# 执行此函数后，tcp_server_socket 会由主动套接字变为被动套接字
tcp_server_socket.listen(128)

# 4、等待接受客户端的连接请求
# 返回值是一个元组  元素 1：客户端的 socket 对象  元素 2：客户端的 IP 地址
client_socket, client_addr = tcp_server_socket.accept()

# 5、收发数据
# print('接收数据：\n', client_socket.recv(1024).decode('utf-8'))  # 接收数据
# str = input('发送数据：\n')
# client_socket.send(str.encode('utf-8')) # 发送数据
# 循环接收数据
while True:
    message = client_socket.recv(1024)
    if len(message) == 0:
        break
    else:
        print('接收数据：\n', message.decode('utf-8'))

# 6、关闭套接字
client_socket.close()
tcp_server_socket.close()
print('\n已释放资源正常退出！')
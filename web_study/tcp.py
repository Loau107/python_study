# 客户端
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

# 4、接收数据
recv_data = tcp_client_socket.recv(1024) # 参数是以字节为单位的数据大小
print('\n接收回复：')
print(recv_data.decode('utf-8'))

# 5、关闭客户端套接字
tcp_client_socket.close()
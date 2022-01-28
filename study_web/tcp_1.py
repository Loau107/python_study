import os
import socket
import threading

client_list = []


def handler_client_request(client_num, tcp_server_socket, pid):
    print(f'--客户端 {client_num + 1} 进入 {client_list[client_num].getpeername()}')
    l = len(client_list)
    for i in range(l):
        if client_list[i] == '':
            continue
        client_list[i].send(f'--客户端 {client_num + 1} 进入 {client_list[client_num].getpeername()}\n'.encode('utf-8'))
    # 选择连接其他客户端
    # client_list[client_num].send('')
    while True:
        message = client_list[client_num].recv(1024)
        # 判断客户是否退出
        if len(message) == 0:
            client_list[client_num].close()
            client_list[client_num] = ''
            print(f'--客户端 {client_num + 1} 退出\n')
            for client in client_list:
                if client == '':
                    continue
                client.send(f'--客户端 {client_num + 1} 退出\n'.encode('utf-8'))
            return
        else:
            message = message.decode('utf-8')
            if message == 'end':
                print(f'\n--客户端 {client_num + 1} 请求关闭服务器！\n')
                client_list[client_num].send('请输入管理员密码:\n'.encode('utf-8'))
                password = client_list[client_num].recv(1024).decode('utf-8')
                client_list[client_num].send(f'{password}\n'.encode('utf-8'))
                if password == '199108':
                    for client in client_list:
                        if client == '':
                            continue
                        client.send('--服务器已关闭!\n'.encode('utf-8'))
                        print(f'--已释放 : {client.getpeername()}')
                        client.close()
                    tcp_server_socket.close()
                    print('\n--服务端正常退出')
                    os.system('kill ' + str(pid))
                else:
                    client_list[client_num].send('密码错误!\n请重新尝试请求!'.encode('uft-8'))
            else:
                print(f'客户端 {client_num + 1} : {message}')
                l = len(client_list)
                for i in range(l):
                    if client_list[i] == '':
                        continue
                    client_list[i].send(f'客户端 {client_num + 1} : {message}\n'.encode('utf-8'))


if __name__ == '__main__':
    sum = 0
    pid = os.getpid()
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(128)
    while True:
        client_socket, client_addr = tcp_server_socket.accept()
        client_list.append(client_socket)
        sub_client = threading.Thread(target=handler_client_request, args=(sum, tcp_server_socket, pid), daemon=True)
        sum += 1
        sub_client.start()
import socket

server = socket.socket()  # 1. 新建socket
server.bind(('127.0.0.1', 8881))  # 2. 绑定IP和端口
server.listen(5)  # 3. 监听连接
s, addr = server.accept()  # 4. 接受连接
print('来自：{}，说了'.format(addr))
content = s.recv(1024)
print(str(content, encoding='utf-8'))  # 接受来自客户端的消息，并编码打印出来
s.close()

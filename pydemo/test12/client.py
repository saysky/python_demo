import socket

client = socket.socket()  # 1. 新建socket
client.connect(('127.0.0.1', 8881))  # 2. 连接服务端
str = input('请输入一句话：')
client.send(bytes(str, encoding='utf-8'))  # 发送内容
client.close()

# -*- coding:UTF-8 -*-

import socket

#第一个参数为ip地址，第二个参数为端口号
HOST, PORT = '', 8888

#创建socket对象。调用socket构造函数
#AF_INET为ip地址族，SOCK_STREAM为流套接字
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置（level,optname,value）
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#将socket绑定到指定地址，第一个参数为ip地址，第二个参数为端口号
listen_socket.bind((HOST, PORT))
#设置最多连接数量
listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT

while True:
    print 'I am waiting for the client......'
    #服务器套接字通过socket的accept方法等待客户请求一个连接
    client_connection, client_address = listen_socket.accept()
	#接收数据的大小
    request = client_connection.recv(1024)
    print request
 
    http_response = """
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
	#关闭与客户端的连接
    client_connection.close()
	
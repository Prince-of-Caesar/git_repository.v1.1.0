# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
import socket
#SOCK_DGRAM意味着你正在创建一个数据报类型的套接字，它使用UDP（用户数据报协议）。
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Trace', b'mary', b'tom']:
    #发送数据
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收到的数据是以字节形式存储的。为了将其转换为字符串形式以便于阅读和处理，使用了.decode('utf-8')的方法。
    #接收数据
    print(s.recv(1024).decode('utf-8'))
s.close()
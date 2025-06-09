# 当我们在浏览器中访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。

# Socket是网络编程的一个抽象概念。而打开一个Socket“网络链接”需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
# 大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

import socket

#创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
# SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
#建立连接：
s.connect(('www.sina.com.cn', 80))
# b表示这是一个字节串（byte string）,将HTTP请求转换为字节形式
# 请求的目标路径（/代表根目录），以及使用的HTTP协议版本（HTTP/1.1）。\r \n是回车 换行符，用于标记行的结束。
#发送数据,方法 路径 协议版本，三者之间都要有空格。
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接受数据：
buffer = []
while True:
    #每次最多接受1k字节：
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
#空字节串b''作为分隔符将这些字节串连接起来。
data = b''.join(buffer)

s.close()

#接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件：
with open('sana.html', 'wb') as f:
    f.write(html)
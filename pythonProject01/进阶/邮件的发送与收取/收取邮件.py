#  parser用于解析原始的电子邮件内容
#  decode_header 函数用于解码电子邮件头部中的字符串，它能够识别并转换多种编码格式到普通的 Unicode 字符串。
#  这对于正确显示带有非ASCII字符的邮件头信息（例如主题、发件人等）特别有用。
#  Header 类，你可以指定使用的字符集以及编码方式（如 base64 或 quoted-printable），这对于构建符合 MIME 标准的邮件尤其重要。
#  email.utils 模块中的一个非常有用的函数，用于解析邮件地址字符串。
#  parseaddr邮件地址字符串中提取出 人名（显示名） 和 邮箱地址。
import poplib
from email.parser import Parser
from email.header import decode_header,Header
from email.utils import parseaddr

def print_email(msg):
    for header in ['From','to','Subject']:
        value = msg.get(header, '')
        if value:
            if header =='Subject':
                value = decode_str(value)
        else:
            hdr,addr = parseaddr(value)
            name = decode_str(hdr)
            value = u'%s <%s>' % (name,addr)
    print('%s: %s' %(header,value))
    # 获取邮件主体信息
    attachment_files = []
    for part in msg.walk():
        # 获取附件名称类型
        file_name = part.get_filename()
        # 获取数据类型
        contentType = part.get_content_type()
        # 获取编码格式
        mycode = part.get_content_charset()
        if file_name:
            h = Header(file_name)
            # 对附件名称进行解码
            dh = decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                # 将附件名称可读化
                filename = decode_str(str(filename, dh[0][1]))
            attachment_files.append(filename)
            # 下载附件
            data = part.get_payload(decode=True)
            # 在当前目录下创建文件
            with open(filename, 'wb') as f:
                # 保存附件
                f.write(data)
        elif contentType == 'text/plain':
            data = part.get_payload(decode=True)
            content = data.decode(mycode)
            print('正文：',content)
        elif contentType == 'text/html':
            data = part.get_payload(decode=True)
            content = data.decode(mycode)
            print('正文：', content)
    print('附件名列表：', attachment_files)

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 接收者邮箱地址
receiverMail = '840588548@qq.com'
# 接收者 QQ 邮箱授权码
authCode = 'akxljawmmrljbfab'
pop3_server = 'pop.qq.com'
# 连接到 POP3 服务器
server = poplib.POP3_SSL(pop3_server, 995)
# 身份认证
server.user(receiverMail)
server.pass_(authCode)
# stat() 返回邮件数量和占用空间
print('邮件数量:%s  占用空间:%s' % server.stat())
# list() 返回所有邮件的编号，lines 存储了邮件的原始文本的每一行
resp, mails, octets = server.list()
index = len(mails)
# 获取最新一封邮件
resp, lines, octets = server.retr(index)
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析邮件
msg = Parser().parsestr(msg_content)
print_email(msg)
# 根据邮件索引号直接从服务器删除邮件
# server.dele(1)
# 关闭连接
server.quit()

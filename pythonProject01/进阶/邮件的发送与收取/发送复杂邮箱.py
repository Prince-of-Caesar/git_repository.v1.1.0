import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#  发送者邮件地址
senderMail = '840588548@qq.com'
authCode = 'akxljawmmrljbfab'

#  接收者邮件地址
receiverMail = '840588548@qq.com'

#  邮件主题
subject = '复杂邮件'
msgRoot = MIMEMultipart('related')  #  构建一个关联型多部分内容的邮件（如 HTML + 图片）
msgRoot['Subject'] = subject  #  设置邮件标题
msgRoot['From'] = senderMail
msgRoot['To'] = receiverMail
msgAtv = MIMEMultipart('alternative')  #  创建一个可包含多个“替代”版本内容的邮件部分（如 plain + html）
msgRoot.attach(msgAtv)  #  邮件内容的各个部分（如正文、图片、附件等）组织成一个完整的邮件结构。

#  html
#  <p>表示一个段落（paragraph）
#  <a>表示一个超链接标签（anchor），用于创建可点击的链接
#  href='https://blog.csdn.net/ityard'	指定链接的目标地址
#  </a></p>  结束标签，表示该元素内容结束
#  src="cid:image"	<img> 标签的 src 属性用于指定图像文件的位置，使用 Content-ID（CID）适用于 HTML 邮件中内嵌图像
html_content = '''
<p>我的博客地址：</p>  
<p><a href='https://blog.csdn.net/ityard'>点击进入我的CSDN</a></p>  
<p>我的公众号二维码：</p>
<p><img src="cid:image"></p> 
'''
html = MIMEText(html_content, 'html', 'utf-8')
msgAtv.attach(html)
#  rb 二进制读取 确保能够完整无误地获取文件中的所有信息
f = open(r'C:\Users\Hasee\Pictures\微信图片_20230820122347.jpg', 'rb')
msgImage = MIMEImage(f.read())
f.close()
msgImage.add_header('Content-ID', '<image>')
msgRoot.attach(msgImage)
# 附件
#  'base64' 表示将文件内容进行 Base64 编码，适合传输非文本数据（如二进制文件）
#  设置该附件的 MIME 类型为 application/octet-stream，意思是“未知的二进制流”
#  设置附件的Disposition显示方式为 attachment（即作为附件下载，而不是直接在邮件中显示）
annex = MIMEText(open('../../test.txt', 'rb').read(), 'base64', 'utf-8')
annex['Content-Type'] = 'application/octet-stream'
annex['Content-Disposition'] = 'attachment; filename="test.txt"'
msgRoot.attach(annex)
try:
#  使用 SMTP_SSL 方法创建一个安全的 SMTP 连接，指定主机为 'smtp.qq.com' 和默认的 SSL 端口。
    server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    print('成功连接到邮件服务器')
#  使用 login 方法进行邮箱认证，需要提供发件人的邮箱地址 (senderMail) 和授权码 (authCode)。
    server.login(senderMail, authCode)
    print('成功登录邮箱')
#  邮件内容 (msgRoot.as_string())。
    server.sendmail(senderMail, receiverMail, msgRoot.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送异常')
finally:
    server.quit()
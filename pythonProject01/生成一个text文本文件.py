# 打开（或创建）一个文本文件，并写入内容
with open("文本文件.txt", "w", encoding="utf-8") as file:
    file.write("1、启动服务器：使用cd命令切换到包含 server.py 文件的目录\n"
               "python3 server.py\n"
               "2、启动客户端：使用cd命令切换到包含 client.py 文件的目录\n"
               "python3 client.py")

print("文本文件已生成！")
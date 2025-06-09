# 打开（或创建）一个文本文件，并写入内容
with open("操作流程.txt", "w", encoding="utf-8") as file:
    file.write("打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序：\r\n"
               "1、启动服务器：使用cd命令切换到包含 server.py 文件的目录\n"
               "python server.py\n"
               "2、启动客户端：使用cd命令切换到包含 client.py 文件的目录\n"
               "python client.py")

print("文本文件已生成！")
# QLite是一种嵌入式数据库，它的数据库就是一个二进制文件。由于SQLite本身是C写的，而且体积很小，
# SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

import sqlite3

#数据库文件是test.db,如果不存在，会自动创建
conn = sqlite3.connect('test.db')

#创建一个游标
cursor = conn.cursor()

#执行一条SQL创建user表
print(cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))'))
#插入一条记录
print(cursor.execute('insert or replace into user (id, name) values (\'1\', \'Miacheal\')'))

#通过rowcount获得插入的行数
print(cursor.rowcount)

#提交事务
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()

# ---------------------------------------------------------------------------------
#试试查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

#执行查询语句：
# Python 无法区分是表示一个单独元素的元组还是仅仅是被括号包围的表达式或值。添加逗号可以消除这种歧义。
cursor.execute('select * from user where id = ?', ('1',))
# 使用Cursor对象执行select语句时，通过fetchall()可以拿到结果集
# 结果集是一个list，每个元素都是一个tuple，对应一行记录。
print(cursor.fetchall())
cursor.close()
conn.close()
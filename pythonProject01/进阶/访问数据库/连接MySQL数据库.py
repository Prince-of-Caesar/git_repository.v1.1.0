# 连接到MySQL服务器的test数据库：
import pymysql

conn = pymysql.connect(user='root', password='linchengda201314', host='localhost', database='test')
cursor = conn.cursor()

#先删表
print(cursor.execute('drop table if exists user'))
# 建user表：
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Tom'])
print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()

#运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭游标和连接：
cursor.close()
conn.close()
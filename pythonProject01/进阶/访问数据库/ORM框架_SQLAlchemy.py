'''
Object-Relational Mapping，把关系数据库的表结构映射到对象上:
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
这就是ORM框架技术
'''

# 在Python中，最有名的ORM框架是SQLAlchemy：
# create_engine: 创建数据库引擎，它是 SQLAlchemy 连接数据库的核心组件。
# sessionmaker: 是一个工厂类，用于创建数据库会话（Session），你可以通过会话对数据库执行操作（如增删改查）。
# declarative_base: 是一个基类，所有你的模型类（对应数据库表）都需要继承它。它允许你通过类定义自动生成数据库表结构。
# 第一步，导入SQLAlchemy，并初始化DBSession：
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#创建对象的基类：
Base = declarative_base()

#定义User对象：
class User(Base):
    #表名：
    __tablename__ = 'user'
    #表结构：
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

#初始化数据库连接：
engine = create_engine('mysql+pymysql://root:linchengda201314@localhost:3306/test')
# bind=engine表示这个 sessionmaker 工厂创建出的所有 Session 对象都会绑定到你之前创建的 engine 上，即使用这个引擎去连接数据库
#创建DBSession类型：
DBSession =sessionmaker(bind=engine)


#有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
session = DBSession()
#创建新User对象：
new_user = User(id='5', name='Bob')
#添加到session:
session.add(new_user)
#提交即保存到数据库:
session.commit()
#关闭session:
session.close()


'''------------------------------------------------------------'''
# SQLAlchemy提供的查询接口如下：
#创建Session:
session = DBSession()
#创建Query查询，filter是where条件，最后调用one()返回为一行，调用all()则返回所有行：
user= session.query(User).filter(User.id=='5').one()
#打印类型和对象的属性：
print('type', type(user))
print('name', user.name)
#关闭会话：
session.close()
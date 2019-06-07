from exts import db
from datetime import datetime
from werkzeug.security import  check_password_hash,generate_password_hash

class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    _password=db.Column(db.String(150),nullable=False)#_为私有属性
    email=db.Column(db.String(50),nullable=False,unique=True)
    join_time=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,password,email):
        self.username=username
        self.password=password#self.password调用的是setter方法
        self.email=email
#密码对外叫做password
#密码对内叫做_password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw_password):
        self._password=generate_password_hash(raw_password)
    def check_password(self,raw_password):
        result=check_password_hash(self.password,raw_password)
        return result
class Cms_User(db.Model):
    __tablename__="cms_user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    _password=db.Column(db.String(150),nullable=False)#_为私有属性
    email=db.Column(db.String(50),nullable=False,unique=True)
    join_time=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,password,email):
        self.username=username
        self.password=password#self.password调用的是setter方法
        self.email=email
#密码对外叫做password
#密码对内叫做_password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw_password):
        self._password=generate_password_hash(raw_password)
    def check_password(self,raw_password):
        result=check_password_hash(self.password,raw_password)
        return result
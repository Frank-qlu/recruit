from flask_script import Manager
from exts import db
from zlzpView import app
from flask_migrate import Migrate,MigrateCommand
from model import Cms_User


manager=Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)
@manager.option("-u","--usename",dest="username")
@manager.option("-p","--password",dest="password")
@manager.option("-e","--email",dest="email")
def create_cms_user(username,email,password):
   user=Cms_User(username=username,email=email,password=password)
   db.session.add(user)
   db.session.commit()
   print("cms用户信息添加成功")
if __name__ == '__main__':
    manager.run()
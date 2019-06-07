from wtforms import Form,StringField,IntegerField,FileField
from flask_wtf.file import FileRequired,FileAllowed
from wtforms.validators import InputRequired,Email,Length,EqualTo
class LoinForm(Form):
    email=StringField(validators=[Email(message="请输入正确的邮箱格式"),InputRequired(message="请输入邮箱")])
    password=StringField(validators=[Length(6,20,message="请输入正确的密码")])
class RegisterForm(Form):
    email = StringField(validators=[Email(message="请输入正确的邮箱格式"),InputRequired(message="请输入邮箱")])
class PasswordForm(Form):
    email = StringField(validators=[Email(message="请输入正确的邮箱格式"),InputRequired(message="请输入邮箱")])
class Cms_loinForm(Form):
    email=StringField(validators=[Email(message="请输入正确的邮箱格式"),InputRequired(message="请输入邮箱")])
    password=StringField(validators=[Length(6,20,message="请输入正确的密码")])
    remember = IntegerField()
# 文件上传验证
class UpLoad(Form):
    photo=FileField(validators=[FileRequired(),FileAllowed(["jpg","gif","png"])])
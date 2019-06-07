#author Frank_Lee
# email=lizhipengqilu@gmail.com
#2019/3/21
from flask import render_template,request,redirect,session,views,url_for,Blueprint,g
from datetime import datetime
import read_data
from exts import db
from model import User
from form import LoinForm,RegisterForm
import yagmail
from blueprint.decorators import login_required

bp=Blueprint("front",__name__)
# 登录你的邮箱
yag = yagmail.SMTP(user='1309485938@qq.com', password='zyvcxlnkzoxkhgcb', host='smtp.qq.com')



class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template("login_index.html",message=message)
    def post(self):
        form=LoinForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session["recruit_config.USER_ID"] = user.id
                session["username"]=user.username
                # session.permanent=timedelta(days=1)
                return redirect(url_for("front.index"))
            else:
                return self.get(message="用户名或者密码错误")
        else:
            return self.get(message=form.errors.popitem()[1][0])
bp.add_url_rule("/",view_func=LoginView.as_view("login"))

class RegisterView(views.MethodView):
    def get(self,message=None):
        return render_template("register.html",message=message)
    def post(self):
        print(request.form.get("email"))
        form=RegisterForm(request.form)
        if form.validate():
            username=request.form.get("username")
            email=form.email.data
            password=request.form.get("password")
            user = User.query.filter_by(email=email).first()
            if user:
                return self.get(message="邮箱已经存在")
            else:
                user1=User(username=username,password=password,email=email)
                db.session.add(user1)
                db.session.commit()
                return redirect("/")
        else:
            return self.get(message=form.errors.popitem()[1][0])
bp.add_url_rule("/register/",view_func=RegisterView.as_view("register"))

class PasswordView(views.MethodView):
    def get(self,message=None):
        return render_template("forget_password.html",message=message)
    def post(self):
        # print(request.form.get("email"))
        form=RegisterForm(request.form)
        if form.validate():
            email=form.email.data
            user = User.query.filter_by(email=email).first()
            if user:
                content = "你的密码是:" + user.password
                # print(user._password,content)
                # 发送邮件
                yag.send(to=[email], subject='网络爬虫招聘信息检索系统密码找回',
                         contents=[content])
                return redirect("/")
            else:
                return self.get(message="请输入正确的注册邮箱")
        else:
            return self.get(message=form.errors.popitem()[1][0])
bp.add_url_rule("/forget_password/",view_func=PasswordView.as_view("forget_password"))

@bp.route('/index/',methods=["POST","GET"],endpoint="index")
@login_required
def hello_world():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        g.username = session.get('username')
        return render_template("search.html")
    else:
        g.username= session.get('username')
        return render_template("index.html")
@bp.route('/ciyun/',methods=["POST","GET"])
@login_required
def ciyun():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        g.username = session.get('username')
        return render_template("search.html")
    else:
        g.username = session.get('username')
        return render_template("ciyun.html")
@bp.route('/educate/',methods=["POST","GET"])
@login_required
def education():
    if request.method=='POST':
       zhiweis=request.form.get("zhiwei")
       zw=read_data.collection.find({"pname":{'$regex': zhiweis}})
       g.zw=zw
       g.username = session.get('username')
       return render_template("search.html")
    else:
        g.master=read_data.master
        g.doctor=read_data.doctor
        g.undergraduate=read_data.count_undergraduate
        g.others=read_data.others
        g.unlimited=read_data.unlimited
        g.college=read_data.college
        g.time=datetime.now()
        g.username = session.get('username')
        return render_template("education.html")
@bp.route("/experience/",methods=["POST","GET"])
@login_required
def work_experience():
    if request.method=='POST':
       zhiweis=request.form.get("zhiwei")
       zw=read_data.collection.find({"pname":{'$regex': zhiweis}})
       g.zw=zw
       g.username = session.get('username')
       return render_template("search.html")
    else:
        g.unrestricted=read_data.unrestricted
        g.one_year=read_data.one_year
        g.three_year=read_data.three_year
        g.five_year=read_data.five_year
        g.username = session.get('username')
        return render_template("experience.html")
@bp.route("/advance/",methods=["POST","GET"])
@login_required
def advance_search():
    if request.method=='POST':

        return "hello world"
    else:
        zw = read_data.collection.find()
        g.zw = zw
        return render_template("advance.html")


@bp.route('/exit/')
def delete():
    session.pop("recruit_config.USER_ID")
    return redirect("/")
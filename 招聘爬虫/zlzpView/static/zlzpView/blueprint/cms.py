from flask import views,render_template,request,session,redirect,Blueprint,g,url_for
from form import Cms_loinForm
from model import Cms_User,User
from .decorators import cms_login_required
import recruit_config
import read_data

bp=Blueprint("cms",__name__,url_prefix="/cms")



class Cms_loginView(views.MethodView):
    def get(self,message=None):
        return render_template("cms/cms_login.html",message=message)
    def post(self):
        form=Cms_loinForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            remember=form.remember.data
            user=Cms_User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session["recruit_config.CMS_USER_ID"]=user.id
                if remember:
                    print("session设置成功")
                    #如果设置session_id=True
                    #那么过期时间是31天
                    session.permanent=True
                return redirect(url_for("cms.cms_index"))
            else:
                return self.get(message='邮箱或者密码错误')

        else:
            print(form.errors)
            return self.get(message=form.errors.popitem()[1][0])
        #("password",[“请输入正确格式的邮箱”])

bp.add_url_rule("/login/",view_func=Cms_loginView.as_view("cms_login"))

@bp.route("/index/",endpoint="cms_index")
@cms_login_required
def cms_index():
    return render_template("cms/cms_index.html")

@bp.route("/user/",endpoint="user")
@cms_login_required
def cms_user():
    user=User.query.all()
    g.user=user
    return render_template("cms/user.html")

@bp.route("/job/",endpoint="job")
@cms_login_required
def cms_job():
    job_data=read_data.collection.find()
    g.job=job_data
    # print(job_data)
    return render_template("cms/job.html")

@bp.route('/exit/')
@cms_login_required
def delete():
    session.pop("recruit_config.CMS_USER_ID")
    return redirect("/")


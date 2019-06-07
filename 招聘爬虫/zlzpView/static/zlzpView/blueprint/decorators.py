from flask import session,redirect,url_for
from functools import wraps
import recruit_config

def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if "recruit_config.USER_ID" in session:
            print(session)
            return func(*args,**kwargs)
        else:
            return redirect(url_for("front.login"))
    return inner
def cms_login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if "recruit_config.CMS_USER_ID" in session:
            return func(*args,**kwargs)
            print(session)
        else:
            return redirect(url_for("cms.cms_login"))
    return inner
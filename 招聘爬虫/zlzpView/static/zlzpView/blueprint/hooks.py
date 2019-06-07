import recruit_config
from flask import session,g
from model import Cms_User
from .cms import bp


@bp.before_request
def before_request():
    if "recruit_config.CMS_USER_ID" in session:
       cms_user_id=session.get("recruit_config.CMS_USER_ID")
       cms_user=Cms_User.query.get(cms_user_id)
       if cms_user:
           # print(cms_user)
           # print("*****************")
           # print(cms_user.username)
           # print("*****************")
           g.cms_user = cms_user

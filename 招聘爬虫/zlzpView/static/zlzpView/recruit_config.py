import os
from redis import StrictRedis
URI="mysql+pymysql://root:123456@localhost:3306/recruit?charset=utf8"
SECRET_KEY=os.urandom(24)
SQLALCHEMY_DATABASE_URI=URI
DEBUG=True
TEMPLATES_AUTO_RELOAD=True
SQLALCHEMY_TRACK_MODIFICATIONS=False
USER_ID="ASASASASASDF"
CMS_USER_ID="ZZZZZZZJAPJOD"
SESSION_TYPE="redis"
SESSION_REDIS=StrictRedis(host='127.0.0.1', port=6379)
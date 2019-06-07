from flask import Flask
from exts import db
import recruit_config
from blueprint import cms_bp
from blueprint import front_bp
from flask_session import Session

app=Flask(__name__)
app.config.from_object(recruit_config)
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
db.init_app(app)#将db和app绑定
Session(app)#装载app到Session


if __name__ == '__main__':
    app.run()
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']='hard to guess string'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:2018@127.0.0.1:3306/flask2018'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

    db.init_app(app)
    bootstrap.init_app(app)

    from .english import english as english_blueprint
    app.register_blueprint(english_blueprint)

    return app

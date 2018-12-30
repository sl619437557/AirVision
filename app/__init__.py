from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db=SQLAlchemy()


def create_app():

    app=Flask(__name__)

    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1205@127.0.0.1:3306/Air'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db = SQLAlchemy(app)

    db.init_app(app)
    bootstrap.init_app(app)

    from .AirViz import airviz as airviz_blueprint
    app.register_blueprint(airviz_blueprint)

    return app

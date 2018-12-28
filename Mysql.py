# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('hello.html')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sl753951@127.0.0.1:3306/Air'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Flask

app.config['SECRET_KEY']='123456'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1205@127.0.0.1:3306/Air'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db = SQLAlchemy(app)


class Airport(db.Model):
    __tablename__ = 'airport2'
    AirportID = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.Text)
    City = db.Column(db.Text)
    Country = db.Column(db.Text)
    IATA = db.Column(db.Text)
    ICAO = db.Column(db.Text)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Altitude = db.Column(db.Integer)
    def __repr(self):
        return '<Airport %r>' %self.name
    
class Routes(db.Model):
    __tablename__='routes2'
    Airline=db.Column(db.Text)
    AirlineID=db.Column(db.Integer)
    SourceAirport=db.Column(db.Text)
    SourceAirportID=db.Column(db.Integer)
    DestinationAirport=db.Column(db.Text)
    DestinationAirportID=db.Column(db.Integer)
    ID=db.Column(db.Integer,primary_key=True)
    def __repr(self):
        return '<Routes %r>' %self.name
    
class Airline(db.Model):
    __tablename__='airline2'
    AirlineID=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.Text)
    IATA=db.Column(db.Text)
    ICAO=db.Column(db.Text)
    Country=db.Column(db.Text)
    def __repr(self):
        return '<Routes %r>' %self.name

#db.create_all()
print(Airport.query.count())
print(Routes.query.count())
print(Airline.query.count())

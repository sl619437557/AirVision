# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy.dialects import mysql
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('hello.html')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sl753951@127.0.0.1:3306/Air'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Flask

app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sl753951@127.0.0.1:3306/Air'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Airport(db.Model):
    __tablename__ = 'airport2'
    AirportID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text)
    City = db.Column(db.Text)
    Country = db.Column(db.Text)
    IATA = db.Column(db.Text)
    ICAO = db.Column(db.Text)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Altitude = db.Column(db.Integer)

    def __repr(self):
        return '<Airport %r>' % self.name


class Routes(db.Model):
    __tablename__ = 'routes2'
    Airline = db.Column(db.Text)
    AirlineID = db.Column(db.Integer)
    SourceAirport = db.Column(db.Text)
    SourceAirportID = db.Column(db.Integer)
    DestinationAirport = db.Column(db.Text)
    DestinationAirportID = db.Column(db.Integer)
    ID = db.Column(db.Integer, primary_key=True)

    def __repr(self):
        return '<Routes %r>' % self.name


class Airline(db.Model):
    __tablename__ = 'airline2'
    AirlineID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text)
    IATA = db.Column(db.Text)
    ICAO = db.Column(db.Text)
    Country = db.Column(db.Text)

    def __repr(self):
        return '<Routes %r>' % self.name

# db.drop_all()
# db.create_all()

print(Airport.query.count())
print(Routes.query.count())
print(Airline.query.count())

# count=db.session.query(Airport).filter(Airport.Country == 'China').count()
# print count
# name = db.session.query(Airport.Name).filter(Airport.Country == 'China').all()
# model = db.session.query(Airport).filter(Airport.Country == 'China').all()
# id = db.session.query(Airport.AirportID).filter(Airport.Country == 'China').all()
# namelist = []
# for i in name:
#     b = str(i)
#     c = b[3:]
#     d = c[:-3]
#     namelist.append(d)
# print namelist

airportModel=Airport.query.filter(Airport.Country == 'China').all()
nodejson=[]
d = {"AirportID":-1,"Country":"","name": ""}
for g in airportModel:
    name=g.Name
    id=g.AirportID
    country=g.Country
    test = d.copy()
    test["name"] = name
    test["AirportID"]=id
    test["Country"]=country
    nodejson.append(test)
print(nodejson)
airportid=[]
edgejson=[]
d = {"source":-1,"target":-1}
for g in airportModel:
    id=g.AirportID
    routesModel=Routes.query.filter(Routes.SourceAirportID==id).all()
    for i in routesModel:
        source=i.SourceAirportID
        target=i.DestinationAirportID
        test=d.copy()
        test["source"]=source
        test["target"]=target
        edgejson.append(test)
    #print(edgejson)
print(len(edgejson))



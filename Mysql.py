# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('hello.html')

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1205@127.0.0.1:3306/Air'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=Flask
db=SQLAlchemy(app)
class airport(db.Model):
    AirportID=db.Column(db.Integer)
    Name=db.Column(db.Text)
    City=db.Column(db.Text)
    Country=db.Column(db.Text)
    IATA=db.Column(db.Text)
    ICAO=db.Column(db.Text)
    Latitude=db.Column(db.Float)
    Longitude=db.Column(db.Float)
    Altitude=db.Column(db.Integer)

    def __init__(self,AirportID,Name,City,Country,IATA,ICAO,Latitude,Longitude,Altitude):
        self.Airport=AirportID
        self.Name=Name
        self.City=City
        self.Country=Country
        self.IATA=IATA
        self.ICAO=ICAO
        self.Latitude=Latitude
        self.Longitude=Longitude
        self.Altitude=Altitude

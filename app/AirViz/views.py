from . import airviz
from flask import render_template
from .. import db


@airviz.route('/airviz',methods=['GET','POST'])
def index():

    nodejson = getNodes()
    edgejson = getEdges()

    return render_template('airviz/airviz.html', nodejson=nodejson, edgejson=edgejson)



def getNodes():
    airportModel = db.Airport.query.filter(db.Airport.Country == 'China').all()
    nodejson = []
    d = {"AirportID": -1, "Country": "", "name": ""}
    for g in airportModel:
        name = g.Name
        id = g.AirportID
        country = g.Country
        test = d.copy()
        test["name"] = name
        test["AirportID"] = id
        test["Country"] = country
        nodejson.append(test)
    return nodejson

def getEdges():
    airportModel = db.Airport.query.filter(db.Airport.Country == 'China').all()
    edgejson = []
    d = {"source": -1, "target": -1}
    for g in airportModel:
        id = g.AirportID
        routesModel = db.Routes.query.filter(db.Routes.SourceAirportID == id).all()
        for i in routesModel:
            source = i.SourceAirportID
            target = i.DestinationAirportID
            test = d.copy()
            test["source"] = source
            test["target"] = target
            edgejson.append(test)
    return edgejson
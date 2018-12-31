from . import airviz
from flask import render_template
from .. import db


@airviz.route('/airviz',methods=['GET','POST'])
def index():

    nodejson = getNodes()
    edgejson = getEdges()

    return render_template('airviz/airviz.html', nodejson=nodejson, edgejson=edgejson)



def getNodes():
    return []

def getEdges():

    return []
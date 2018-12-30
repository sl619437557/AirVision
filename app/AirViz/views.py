from . import airviz
from flask import render_template



@airviz.route('/airviz',methods=['GET','POST'])
def index():
    #这里调用方法，传给nodejson edgejson
    nodejson = getNodes()
    edgejson = getEdges()

    return render_template('airviz/airviz.html', nodejson=nodejson, edgejson=edgejson)


#这里写获得节点的方法
def getNodes():

    return []


#这里写获得边的方法
def getEdges():

    return []
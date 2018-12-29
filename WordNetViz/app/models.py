from . import db
class English(db.Model):
    __tablename__='map_enword'
    id=db.Column(db.Integer,primary_key=True)
    english=db.Column(db.String(64))
    pt=db.Column(db.String(64))
    chinese=db.Column(db.String(64))
    flag=db.Column(db.String(64))

class News(db.Model):
    __tablename__='cucnews'
    ID=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    newsfrom=db.Column(db.String(255))
    newsdate=db.Column(db.String(50))
    contents=db.Column(db.String(10000))
    newscount=db.Column(db.Integer)
    newsurl=db.Column(db.String(255))
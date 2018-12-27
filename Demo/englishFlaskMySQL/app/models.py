from . import db
class English(db.Model):
    __tablename__='map_enword'
    id=db.Column(db.Integer,primary_key=True)
    english=db.Column(db.String(64))
    pt=db.Column(db.String(64))
    chinese=db.Column(db.String(64))
    flag=db.Column(db.String(64))

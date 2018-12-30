from .. import db

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
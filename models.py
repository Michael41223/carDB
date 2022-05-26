from main import db

class Cars(db.Model):
    __tablename__ = 'cars'

    carId = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String())
    model = db.Column(db.Integer)
    engine = db.Column(db.String())
    carimage = db.Column(db.String())
    engineimage = db.Column(db.String())

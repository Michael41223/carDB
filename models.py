from main import db

class Cars(db.Model):
    __tablename__ = 'Cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.String(10))
    engine = db.Column(db.String(50))
    carimage = db.Column(db.Integer)
    engineimage = db.Column(db.Integer)

from main import db

class Cars(db.Model):
    __tablename__ = 'Cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    description = db.Column(db.String())
    carimage = db.Column(db.String(80))
    engineimage = db.Column(db.String(80))

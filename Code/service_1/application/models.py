from application import db

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30), nullable=False)
    weather = db.Column(db.String(30), nullable=False)
    suggestion = db.Column(db.String(255), nullable=False) 

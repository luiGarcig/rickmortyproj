from src.models import db

class Locations(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    dimension = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Location {self.name}>"




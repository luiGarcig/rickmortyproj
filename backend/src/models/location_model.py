from sqlalchemy.ext.hybrid import hybrid_property
from src.models import db, ma

class Locations(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    dimension = db.Column(db.String(100), nullable=True)

    native = db.relationship(
        "Characters",
        foreign_keys="Characters.origin_id",
        back_populates="origin",
        lazy="dynamic",
        uselist=True,
    )

    residents = db.relationship(
        "Characters",
        foreign_keys="Characters.location_id",
        back_populates="location",
        lazy="dynamic",
        uselist=True,
    )

    @hybrid_property
    def residents_count(self) -> int:
        return self.residents.count()

    def __repr__(self):
        return f"<Location {self.name}>"

class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()
    residents_count = ma.Integer()


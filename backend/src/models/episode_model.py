from src.models import db, ma

class Episodes(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(50), nullable=False)
    air_date = db.Column(db.Date, nullable=False)
    episode = db.Column(db.String(50), nullable=False)

    characters = db.relationship(
        "Characters",
        secondary="characters_episodes",
        back_populates="episodes",
        lazy="selectin",
    )

    def __repr__(self):
        return f"<Episode {self.name}>"

class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()



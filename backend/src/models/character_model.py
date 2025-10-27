
from src.models import db, ma
from src.models.character_episode_model import characters_episodes


class Characters(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)

    origin_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=True)


    episodes = db.relationship(
        "Episodes",
        secondary=characters_episodes,
        back_populates="characters"
    )

    def __repr__(self):
        return f"<Character {self.name}>"



class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()  


class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    status = ma.String()
    type = ma.String()
    gender = ma.String()
    image = ma.String()
    last_episode = ma.Method("get_last_episode") 


    def get_last_episode(self, obj):
        ep = getattr(obj, "last_episode", None)
        return EpisodeOutput().dump(ep) if ep else None


class EveryCharacterOutput(ma.Schema):
    name = ma.String()
    species = ma.String()
    image = ma.String()

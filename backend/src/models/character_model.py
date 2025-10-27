from src.models import db, ma
from src.models.character_episode_model import characters_episodes
from src.models.location_model import Locations

class Characters(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)

    origin_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=True)

    episodes = db.relationship(
        "Episodes",
        secondary=characters_episodes,
        back_populates="characters"
    )

    origin = db.relationship(
        "Locations",
        primaryjoin="Characters.origin_id == Locations.id",
        foreign_keys=[origin_id],
        lazy="joined",
        viewonly=False,
    )

    location = db.relationship(
        "Locations",
        primaryjoin="Characters.location_id == Locations.id",
        foreign_keys=[location_id],
        lazy="joined",
        viewonly=False,
    )

    def __repr__(self):
        return f"<Character {self.name}>"


class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()  

class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()

class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    status = ma.String()
    type = ma.String()
    gender = ma.String()
    image = ma.String()
    last_episode = ma.Method("get_last_episode") 
    origin = ma.Method("get_origin")
    location = ma.Method("get_location")

    def get_last_episode(self, obj):
        episode = getattr(obj, "last_episode", None)
        return EpisodeOutput().dump(episode) if episode else None

    def get_origin(self, obj):
        origin = getattr(obj, "origin", None)
        return LocationOutput().dump(origin) if origin else None

    def get_location(self,obj):
        location = getattr(obj, "location", None)
        return LocationOutput().dump(location) if location else None
    
class EveryCharacterOutput(ma.Schema):
    name = ma.String()
    species = ma.String()
    image = ma.String()

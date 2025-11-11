from src.models import db, ma
from sqlalchemy.ext.hybrid import hybrid_property

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
        secondary="characters_episodes",
        back_populates="characters"
    )

    origin = db.relationship(
        "Locations",
        foreign_keys=[origin_id],
        back_populates='native',
        uselist=False,
        lazy=True
    )

    location = db.relationship(
        "Locations",
        foreign_keys=[location_id],
        back_populates='residents',
        uselist=False,
        lazy=True,
    )

    @hybrid_property
    def last_episode(self) -> int:
        episodes_list = self.episodes

        if not episodes_list:
            return None
 
        last_episode = max(episodes_list, key=lambda e: (e.id or 0))
 
        return last_episode

    def __repr__(self):
        return f"<Character {self.name}>"

class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    status = ma.String()
    type = ma.String()
    gender = ma.String()
    image = ma.String()
    last_episode = ma.Nested("EpisodeOutput") 
    origin = ma.Nested("LocationOutput")
    location = ma.Nested("LocationOutput")

class CharacterListOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    species = ma.String()
    status = ma.String()
    image = ma.String()

class CharacterPaginationOutput(ma.Schema):
    page = ma.Integer()
    per_page = ma.Integer()
    total = ma.Integer()
    total_pages = ma.Integer()
    items = ma.Nested("CharacterListOutput", many=True)

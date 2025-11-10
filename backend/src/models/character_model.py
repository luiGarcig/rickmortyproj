from src.models import db, ma

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
    last_episode = ma.Method("get_last_episode") 
    origin = ma.Nested("LocationOutput")
    location = ma.Nested("LocationOutput")

    def get_last_episode(self, obj):
        if not getattr(obj, "episodes", None):
            return None
        ep = max(obj.episodes, key=lambda e: e.id)
        from src.models.episode_model import EpisodeOutput
        return EpisodeOutput().dump(ep)

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
    items = ma.Nested("CharacterOutput", many=True)

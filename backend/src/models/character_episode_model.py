
from src.models import db

characters_episodes = db.Table(
    "characters_episodes",
    db.Column("character_id", db.Integer, db.ForeignKey("characters.id"), primary_key=True),
    db.Column("episode_id", db.Integer, db.ForeignKey("episodes.id"), primary_key=True),
)


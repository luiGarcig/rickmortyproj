from sqlalchemy.orm import joinedload
from src.models import db
from src.models.character_model import Characters
from src.models.episode_model import Episodes
from src.models.character_episode_model import characters_episodes
from sqlalchemy import asc, desc


class CharacterRepository:

    def get_all_characters(self, name: str | None, limit: int, offset: int):
        query = Characters.query.options(
            joinedload(Characters.origin),
            joinedload(Characters.location),
        )
        if name:
            query = query.filter(Characters.name.ilike(f"%{name}%"))
        return query.order_by(Characters.id.asc()).limit(limit).offset(offset).all()    

    def get_character_by_id(self, id: int):
        return (
            Characters.query.options(
                joinedload(Characters.episodes),
                joinedload(Characters.origin),
                joinedload(Characters.location),
            )
            .get(id)
        )

    def count_characters(self, name: str | None):
        query = Characters.query
        if name:
            query = query.filter(Characters.name.ilike(f"%{name}%"))
        return query.count()

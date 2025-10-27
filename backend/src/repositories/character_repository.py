
from src.models import db
from src.models.character_model import Characters
from src.models.episode_model import Episodes
from src.models.character_episode_model import characters_episodes
from sqlalchemy import asc, desc


class CharacterRepository:

    def find_characters(self, name=None, limit=20, offset=0):
        try:
            query = Characters.query.order_by(asc(Characters.id))

            if name:
                query = query.filter(Characters.name.ilike(f"%{name}%"))

            result = query.limit(limit).offset(offset).all()
            return result

        except Exception:
            db.session.rollback()
            raise

    def character_detail(self, id: int):
        try:
            character = db.session.get(Characters, id)
            if not character:
                return None

            last_ep = (
                db.session.query(Episodes)
                .join(characters_episodes, Episodes.id == characters_episodes.c.episode_id)
                .filter(characters_episodes.c.character_id == character.id)
                .order_by(desc(Episodes.air_date), desc(Episodes.id))
                .first()
            )

            setattr(character, "last_episode", last_ep)
            return character

        except Exception:
            db.session.rollback()
            raise


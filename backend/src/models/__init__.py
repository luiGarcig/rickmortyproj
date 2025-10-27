from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from src.models.character_episode_model import characters_episodes
from src.models.character_model import Characters
from src.models.episode_model import Episodes
from src.models.location_model import Locations


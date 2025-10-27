
from src.repositories.character_repository import CharacterRepository
from src.models.character_model import CharacterOutput, EveryCharacterOutput


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()
        self.character_output = CharacterOutput()  
        self.every_character_output = EveryCharacterOutput()

    def find_characters(self, name=None, page=1):
        try:
            per_page = 20
            offset = (page - 1) * per_page

           
            characters = self.character_repository.find_characters(
                name=name,
                limit=per_page,
                offset=offset
            )

           
            data = self.every_character_output.dump(characters, many=True)

            return {
                "page": page,
                "per_page": per_page,
                "count": len(characters),
                "data": data
            }
        except Exception as e:
            raise e

    def character_detail(self, id):
        try:
            character = self.character_repository.character_detail(id)
            if not character:
                return {"error": "Character not found"}, 404

          
            data = self.character_output.dump(character)

            return {"data": data}, 200
        except Exception as e:
            raise e


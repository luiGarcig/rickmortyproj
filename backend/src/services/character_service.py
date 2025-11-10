from math import ceil
from src.repositories.character_repository import CharacterRepository
from src.models.character_model import CharacterOutput, CharacterPaginationOutput
from src.utils.api_response import ApiResponse
from werkzeug.exceptions import NotFound

class CharacterService:
    def __init__(self):
        self.character_repository = CharacterRepository()
        self.character_output = CharacterOutput()
        self.character_list_output = CharacterPaginationOutput()


    def get_all_characters(self, name: str | None = None, page: int = 1, per_page: int = 20):
        offset = (page - 1) * per_page

        characters = self.character_repository.get_all_characters(
            name=name,
            limit=per_page,
            offset=offset,
        )

        total = self.character_repository.count_characters(name=name)
        
        pagination = {
            "items": characters,
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": ceil(total / per_page) if per_page else 0,
        }

        pagination = self.character_list_output.dump(pagination)

        return pagination

    def get_character_by_id(self, id: int):
        character = self.character_repository.get_character_by_id(id)
        if character is None:
            raise NotFound
        data = self.character_output.dump(character)

        return data

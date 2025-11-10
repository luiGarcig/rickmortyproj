from flask import jsonify, request
from src.services.character_service import CharacterService
from src.utils.api_response import ApiResponse
from werkzeug.exceptions import NotFound

class CharacterController:
    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self):
        try:
            name = request.args.get("name", default=None, type=str)
            page = request.args.get("page", default=1, type=int)
            per_page = request.args.get("per_page", default=20, type=int)

            data = self.character_service.get_all_characters(name=name, page=page, per_page=per_page)
            return ApiResponse.success(
                status_code=200,
                message="funcionalidade get_all_characters funcionando",
                data=data,
            )
        except Exception:
            return ApiResponse.error(
                status_code=500,
                message="erro na funcionalidade get_all_characters",
                data=None,
            )

    def get_character_by_id(self, id):
        try:
            data= self.character_service.get_character_by_id(id)
            return ApiResponse.success(
                status_code=200,
                message="character found",
                data=data
            )
            
        except NotFound as e:
            return ApiResponse.error(
                status_code=404,
                message=f"character not found: {str(e)}",
                data=None
            )

        except Exception:
            return ApiResponse.error(
                status_code=500,
                message="deu erro na função get_character_by_id",
                data=None
            )


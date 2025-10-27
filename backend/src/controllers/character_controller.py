from flask import jsonify, request 
from src.services.character_service import CharacterService

class CharacterController:
    def __init__(self):
        self.character_service = CharacterService()

    def find_characters(self):
        try:
            name = request.args.get("name", default=None, type=str)
            page = request.args.get("page", default=1, type=int)

            data = self.character_service.find_characters(name=name, page=page)

            return jsonify(data), 200   
        except Exception as e:  
            print(e)
            return jsonify({
                "erro": "deu erro na função find_characters"
            }), 500

    def character_detail(self, id):
        try:
            data = self.character_service.character_detail(id)
            return jsonify(data), 200  
        except Exception as e:  
            print(e)
            return jsonify({
                "erro": "deu erro na função character_detail"
            }), 500

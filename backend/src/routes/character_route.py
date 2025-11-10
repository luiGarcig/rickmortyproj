from flask import Blueprint
from src.controllers.character_controller import CharacterController

character_bp = Blueprint('character_bp', __name__)
character_controller = CharacterController()

@character_bp.route('/getAllCharacters', methods=['GET'])
def get_all_characters():
    return character_controller.get_all_characters()

@character_bp.route('/getCharacter/<int:id>', methods=['GET'])
def get_character_by_id(id):
    return character_controller.get_character_by_id(id)



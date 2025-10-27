from flask import Blueprint
from src.controllers.character_controller import CharacterController

character_bp = Blueprint('character_bp', __name__)
character_controller = CharacterController()

@character_bp.route('/findCharacter', methods=['GET'])
def find_characters():
    return character_controller.find_characters()

@character_bp.route('/characterDetail/<int:id>', methods=['GET'])
def character_detail(id):
    return character_controller.character_detail(id)



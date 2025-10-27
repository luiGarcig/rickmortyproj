from flask import Flask, jsonify
from src.models import db
from config.settings import DATABASE_URI
from src.routes.character_route import character_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

app.register_blueprint(character_bp, url_prefix='/character')

if __name__ == "__main__":
    app.run(debug=True)

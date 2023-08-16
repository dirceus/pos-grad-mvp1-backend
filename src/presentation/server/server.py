from flask import Flask
from flask_cors import CORS

from src.presentation.rest_api.questao_controller import questao_router_bp

app = Flask(__name__)
CORS(app)


# Register Blueprints
app.register_blueprint(questao_router_bp)
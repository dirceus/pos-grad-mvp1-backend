from flask import Flask
from src.presentation.rest_api.questao_controller import questao_router_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(questao_router_bp)
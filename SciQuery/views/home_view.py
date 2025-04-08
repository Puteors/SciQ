from flask import Blueprint
from utils import success_response

# Create a Blueprint for home routes
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return success_response(
        message="Neo4j + Flask API is working!"
    ) 
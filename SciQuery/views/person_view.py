from flask import Blueprint, request
from utils import success_response, error_response, Q

# Create a Blueprint for person routes
person_bp = Blueprint('person', __name__)

@person_bp.route('/create_person', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        name = data.get('name')
        if not name:
            return error_response("Name is required", 400)
            
        query = "CREATE (p:Person {name: $name}) RETURN p"
        result = Q(query, {"name": name})

        return success_response(result, "Person created successfully")
    except Exception as e:
        return error_response(str(e), 500)

@person_bp.route('/get_people', methods=['GET'])
def get_people():
    try:
        query = "MATCH (p:Person) RETURN p.name AS name"
        result = Q(query)
        return success_response(result)
    except Exception as e:
        return error_response(str(e), 500) 
from flask import Flask
from dotenv import load_dotenv
from SciQuery.utils.neo4j_connector import Neo4jConnection
import os
# Import blueprints from views
from views.home_view import home_bp
from views.person_view import person_bp

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get Neo4j connection details from environment variables
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

neo4j_conn = Neo4jConnection(neo4j_uri, neo4j_user, neo4j_password)

# Register blueprints and pass the Neo4j connection
app.register_blueprint(home_bp, url_prefix='/api')
app.register_blueprint(person_bp, url_prefix='/api')

# Make Neo4j connection available to all views
app.config['neo4j_conn'] = neo4j_conn

if __name__ == '__main__':
    app.run(debug=True)


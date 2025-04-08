from flask import current_app

def Q(query, params=None):
    neo4j_conn = current_app.config['neo4j_conn']
    return neo4j_conn.query(query, params or {}) 
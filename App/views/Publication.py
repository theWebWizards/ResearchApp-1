from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    CreatePublication, 
    update_publication,
    get_all_publications,
    get_all_publication_json,
    delete_publication,
)

publication_views = Blueprint('publication_views', __name__, template_folder='../templates')


@publication_views.route('/publications', methods=['GET'])
def get_publication_page():
    publications = get_all_publications()
    return render_template('publications.html', publications=publications)

@publication_views.route('/api/publications', methods=['GET'])
def get_publication_action():
    publications = get_all_publication_json()
    return jsonify(publications)

@publication_views.route('/api/users', methods=['POST'])
def create_publication_action():
    data = request.json
    create_publication(data['title'], data['content'], data['author'], data['authorcreds'], data['type'])
    return jsonify({'message': f"publication {data['title']} created"})


#@publication_views.route('/identify', methods=['GET'])
#@jwt_required()
#def identify_user_action():
    #return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

@publication_views.route('/api/updatepublication', methods=['PUT'])
def update_publication_action():
    data = request.json
    update_publication(data['id'], data['content'])
    return jsonify({'message': f"publication {data['id']} updated"})

@publication_views.route('/api/deletepublication', methods=['DELETE'])
def update_publication_action():
    data = request.json
    delete_publication(data['id'])
    return jsonify({'message': f"publication {data['id']} deleted"})
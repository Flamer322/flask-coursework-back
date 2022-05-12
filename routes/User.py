from flask import Blueprint, request, Response
from models.User import User
from settings import db
import json

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_json = []
    for user in users:
        users_json.append({
            'id': user.id,
            'email': user.email,
            'password': user.password
        })
    response = Response(
        response=json.dumps(users_json),
        status=200,
        mimetype='application/json'
    )
    return response


@users.route('/users', methods=['POST'])
def add_user():
    user_json = json.loads(request.get_data())
    new_user = User(email=user_json['email'], password=user_json['password'])
    db.session.add(new_user)
    db.session.commit()
    response = Response(
        response=str(new_user.id),
        status=200,
        mimetype='text/plain'
    )
    return response

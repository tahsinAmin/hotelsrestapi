from flask import Blueprint, jsonify, request
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from werkzeug.security import check_password_hash, generate_password_hash
from src.database import User, db
auth = Blueprint("auth", __name__, url_prefix='/api/v1/auth')


@auth.post('/register')
def register():
    username = request.json['username']
    password=request.json['password']

    if len(username) < 2:
        return jsonify({'error':"Username is too short"}), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
      return jsonify({'error':"Username should be alphanumeric"}), HTTP_400_BAD_REQUEST

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': "username is taken"}), HTTP_409_CONFLICT

    if len(password) < 2:
        return jsonify({'error':"Password is too short"}), HTTP_400_BAD_REQUEST

    pwd_hash= generate_password_hash(password)
    user=User(username=username, password=pwd_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({
      'mesage': 'user created',
      'user': {
          'username':username
      }
    }), HTTP_201_CREATED

@auth.get("/me")
def me():
  return jsonify({"user":"me"})

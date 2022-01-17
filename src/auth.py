import email
from os import access
from flask import Blueprint, jsonify, request
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
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

@auth.post('/login')
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')

    user=User.query.filter_by(username=username).first()

    if user:
      is_pass_correct= check_password_hash(user.password, password)

      if is_pass_correct:
        refresh = create_refresh_token(identity=user.id)
        access = create_access_token(identity=user.id)

        return jsonify({
          'refresh': refresh,
          'access': access,
          'username':username
        }), HTTP_200_OK

    return jsonify({
      'error': "Wrong Credentials"
    }), HTTP_401_UNAUTHORIZED
    

@auth.get("/me")
def me():
  return jsonify({"user":"me"})

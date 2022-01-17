from crypt import methods
from flask import Blueprint, jsonify
import validators

hotels = Blueprint("hotels", __name__, url_prefix='/api/v1/hotels')

@hotels.route('/', methods=['POST', 'GET'])
def bookmarks():



@hotels.get('/')
def get_all():
  return jsonify({"hotels":[]})

@hotels.get("/me")
def me():
  return jsonify({"user":"me"})

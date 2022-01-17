from flask import Blueprint, jsonify

hotels = Blueprint("hotels", __name__, url_prefix='/api/v1/hotels')


@hotels.get('/')
def get_all():
  return jsonify({"hotels":[]})

@hotels.get("/me")
def me():
  return jsonify({"user":"me"})

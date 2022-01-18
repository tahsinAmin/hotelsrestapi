from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from flask import Blueprint, request
from flask.json import jsonify
# import validators
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.database import Hotel, db
from flasgger import swag_from

hotels = Blueprint("hotels", __name__, url_prefix='/api/v1/hotels')


@hotels.get('/')
@jwt_required()
@swag_from('./docs/hotels/all.yaml')
def handle_hotels():
    current_user = get_jwt_identity() # this gives us the id
    hotels = Hotel.query.filter_by(user_id=current_user)
    data = []
    for hotel in hotels:
      data.append({
        'id':hotel.id,
        'title':hotel.title,
        'price':hotel.price,
        'review':hotel.review,
        'location':hotel.location,
        'amenities':hotel.amenities,
        'image_link':hotel.image_link
      })

    return jsonify({'data': data}), HTTP_200_OK

@hotels.get("/<int:id>")
@jwt_required()
@swag_from('./docs/hotels/byid.yaml')
def get_hotel(id):
    current_user = get_jwt_identity()
    hotel = Hotel.query.filter_by(user_id=current_user, id=id).first()

    if not hotel:
       return jsonify({"message":"Hotel not found"}), HTTP_404_NOT_FOUND
    
    return jsonify({
              'id':hotel.id,
              'title':hotel.title,
              'price':hotel.price,
              'review':hotel.review,
              'location':hotel.location,
              'amenities':hotel.amenities,
              'image_link':hotel.image_link
            }), HTTP_200_OK

@hotels.get("/sort")
@jwt_required()
def sort_hotel():
    current_user = get_jwt_identity()
    hotels = Hotel.query.filter_by(user_id=current_user).order_by(Hotel.price)
    data = []
    for hotel in hotels:
          data.append({
            'id':hotel.id,
            'title':hotel.title,
            'price':hotel.price,
            'review':hotel.review,
            'location':hotel.location,
            'amenities':hotel.amenities,
            'image_link':hotel.image_link
          })

    return jsonify({'data': data}), HTTP_200_OK

@hotels.get("/<string:search_sth>")
@jwt_required()
@swag_from('./docs/hotels/each.yaml')
def get_hotel_by_name(search_sth):
    current_user = get_jwt_identity()

    hotels = Hotel.query.filter_by(user_id=current_user).filter(Hotel.title.ilike(f'%{search_sth}%')).all()

    if not hotels:
       hotels = Hotel.query.filter(Hotel.amenities.ilike(f'%{search_sth}%')).all()

    data = []
    for hotel in hotels:
          data.append({
            'id':hotel.id,
            'title':hotel.title,
            'price':hotel.price,
            'review':hotel.review,
            'location':hotel.location,
            'amenities':hotel.amenities,
            'image_link':hotel.image_link
          })

    return jsonify({'data': data}), HTTP_200_OK

@hotels.get("/me")
def me():
  return jsonify({"user":"me"})

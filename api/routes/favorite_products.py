import requests

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.favorite_products import FavoriteProducts, FavoriteProductsSchema
from api.utils.database import db

favorite_product_routes = Blueprint('favorite_product_routes', __name__)

@favorite_product_routes.route('/<int:client_id>/favorite/products', methods=['POST'])
@jwt_required
def create_favorite_product(client_id):
    try:
        data = request.get_json()
        response = requests.get('http://challenge-api.luizalabs.com/api/product/{}/'.format( data['id']))
        if response.status_code == 404:
            return response_with(resp.SERVER_ERROR_PRODUCT_404)
        fetched = FavoriteProducts.query.filter_by(client_id=client_id).filter_by(id=data['id']).first()
        if fetched is not None:
            return response_with(resp.DUPLICATE_FAVORITE_PRODUCT_422)
        data['client_id'] = client_id
        favorite_products_schema = FavoriteProductsSchema()
        favorite_product = favorite_products_schema.load(data)
        result = favorite_products_schema.dump(favorite_product.create())
        return response_with(resp.SUCCESS_201, value={'favorite_product': result})
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422)

@favorite_product_routes.route('/<int:client_id>/favorite/products', methods=['GET'])
@jwt_required
def get_favorite_products(client_id):
    fetched = FavoriteProducts.query.filter_by(client_id=client_id)
    favorite_products_schema = FavoriteProductsSchema(many=True, only=['id', 'title', 'brand', 'image', 'price', 'reviewScore'])
    favorite_products = favorite_products_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'favorite_products': favorite_products})

@favorite_product_routes.route('/<int:client_id>/favorite/products/<product_id>', methods=['GET'])
@jwt_required
def get_favorite_product(client_id, product_id):
    fetched = FavoriteProducts.query.filter_by(client_id=client_id).filter_by(id=product_id).first()
    if fetched is None:
        return response_with(resp.SERVER_ERROR_PRODUCT_404)
    favorite_products_schema = FavoriteProductsSchema()
    favorite_product = favorite_products_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'favorite_product': favorite_product})
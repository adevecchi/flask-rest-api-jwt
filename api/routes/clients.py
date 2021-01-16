from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required

from sqlalchemy.exc import IntegrityError

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.clients import Client, ClientSchema
from api.utils.database import db

client_routes = Blueprint('client_routes', __name__)

@client_routes.route('/', methods=['POST'])
@jwt_required
def create_client():
    try:
        data = request.get_json()
        client_schema = ClientSchema()
        client = client_schema.load(data)
        result = client_schema.dump(client.create())
        return response_with(resp.SUCCESS_201, value={'client': result})
    except IntegrityError as er:
        return response_with(resp.DUPLICATE_EMAIL_422)
    except Exception as e:
        return response_with(resp.INVALID_INPUT_422)

@client_routes.route('/', methods=['GET'])
@jwt_required
def get_client_list():
    fetched = Client.query.all()
    client_schema = ClientSchema(many=True, only=['id', 'name', 'email'])
    clients = client_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"clients": clients})

@client_routes.route('/<int:client_id>', methods=['GET'])
@jwt_required
def get_client(client_id):
    fetched = Client.query.get_or_404(client_id)
    client_schema = ClientSchema()
    client = client_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"client": client})

@client_routes.route('/<int:id>', methods=['PUT'])
@jwt_required
def update_client(id):
    data = request.get_json()
    get_client = Client.query.get_or_404(id)
    get_client.name = data['name']
    get_client.email = data['email']
    db.session.add(get_client)
    db.session.commit()
    client_schema = ClientSchema()
    client = client_schema.dump(get_client)
    return response_with(resp.SUCCESS_200, value={"client": client})

@client_routes.route('/<int:id>', methods=['DELETE'])
@jwt_required
def delete_client(id):
    get_client = Client.query.get_or_404(id)
    db.session.delete(get_client)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
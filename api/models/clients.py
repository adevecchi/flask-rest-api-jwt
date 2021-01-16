from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from passlib.hash import pbkdf2_sha256 as sha256

from api.utils.database import db
from api.models.favorite_products import FavoriteProductsSchema

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    favorite_products = db.relationship('FavoriteProducts', backref='Client', cascade='all, delete-orphan')

    def __init__(self, name, email, favorite_products=[]):
        self.name = name
        self.email = email
        self.favorite_products = favorite_products
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class ClientSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Client
        sqla_session = db.session
    
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    favorite_products = fields.Nested(FavoriteProductsSchema, many=True, only=['id', 'title', 'brand', 'image', 'price', 'reviewScore'])
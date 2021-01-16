from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from api.utils.database import db

class FavoriteProducts(db.Model):
    __tablename__ = 'favorite_products'

    favorite_prod_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(36), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    reviewScore = db.Column(db.Float())

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def __init__(self, id, title, brand, image, price, reviewScore=None, client_id=None):
        self.id = id
        self.title = title
        self.brand = brand
        self.image = image
        self.price = price
        self.reviewScore = reviewScore
        self.client_id = client_id
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class FavoriteProductsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = FavoriteProducts
        sqla_session = db.session
    
    favorite_prod_id = fields.Integer(dump_only=True)
    id = fields.String(required=True)
    title = fields.String(required=True)
    brand = fields.String(required=True)
    image = fields.String(required=True)
    price = fields.Float(required=True)
    reviewScore = fields.Float()
    client_id = fields.Integer()
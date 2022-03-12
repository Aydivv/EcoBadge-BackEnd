import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _db
import datetime as _dt

class User(_db.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String(255), unique=True, index=True)
    fName = _sql.Column(_sql.String(255))
    lName = _sql.Column(_sql.String(255))

    reviews = _orm.relationship("Review", back_populates="reviewer")

class Review(_db.Base):
    __tablename__ = "reviews"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    content = _sql.Column(_sql.String(255),index=True,)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    business_id = _sql.Column(_sql.Integer, _sql.ForeignKey("business.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    reoly_of = _sql.Column(_sql.Integer, default=_sql.null)
    
    reviewer = _orm.relationship("User", back_populates="reviews")
    of = _orm.relationship("Business", back_populates="reviews")

class Business():
    __tablename__ = "business"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(255), index=True)
    address = _sql.Column(_sql.String(255))
    postcode = _sql.Column(_sql.String(255))
    number = _sql.Column(_sql.String(255))
    email = _sql.Column(_sql.String(255))
    website = _sql.Column(_sql.String(255))
    cuisine = _sql.Column(_sql.String(255))
    
    score = _orm.relationship("Score", back_populates="business")
    reviews = _orm.relationship("Review", back_populates="of")

class Score():
    __tablename__ = "score"
    id = _sql.Column(_sql.Integer, primary_key=True, index = True)
    business_id = _sql.Column(_sql.Integer, _sql.ForeignKey("business.id"), primary_key=True)
    score = _sql.Column(_sql.Integer)
    tier = _sql.Column(_sql.String(20))
    vegan = _sql.Column(_sql.Boolean)
    singleUsePlastic = _sql.Column(_sql.Boolean)
    foodwasteCollection = _sql.Column(_sql.Boolean)
    localProduce = _sql.Column(_sql.Boolean)

    business = _orm.relationship("Business", back_populates="score")


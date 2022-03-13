import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _db
import datetime as _dt

class User(_db.Base):
    __tablename__ = "user"
    id = _sql.Column(_sql.String(50), primary_key=True, index=True, autoincrement=False)
    email = _sql.Column(_sql.String(255), unique=True, index=True)
    name = _sql.Column(_sql.String(255))
    priority = _sql.Column(_sql.Integer)


class Business():
    __tablename__ = "business"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(255), index=True)
    address = _sql.Column(_sql.String(255))
    postcode = _sql.Column(_sql.String(255))
    number = _sql.Column(_sql.String(255))
    email = _sql.Column(_sql.String(255))
    desc = _sql.Column(_sql.String(255))
    website = _sql.Column(_sql.String(255))
    cuisine = _sql.Column(_sql.String(255))
    scored = _sql.Column(_sql.Boolean)
    
    

class Review(_db.Base):
    __tablename__ = "reviews"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    content = _sql.Column(_sql.String(255),index=True,)
    user_id = _sql.Column(_sql.String(50), _sql.ForeignKey("users.id"))
    business_id = _sql.Column(_sql.Integer, _sql.ForeignKey("business.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    reply_of = _sql.Column(_sql.Integer, default=_sql.null)
    
  
    

class Score():
    __tablename__ = "score"
    business_id = _sql.Column(_sql.Integer, _sql.ForeignKey("business.id"), primary_key=True, index=True)
    score = _sql.Column(_sql.Integer)
    vegan = _sql.Column(_sql.Boolean)
    singleUsePlastic = _sql.Column(_sql.Boolean)
    foodwasteCollection = _sql.Column(_sql.Boolean)
    localProduce = _sql.Column(_sql.Boolean)
    latest = _sql.Column(_sql.Boolean)
    dateOfScore = _sql.Column(_sql.DateTime, default = _dt.datetime.utcnow, primary_key=True,index=True)

    


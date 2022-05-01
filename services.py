import database as _db
import sqlalchemy.orm as _orm
import schemas as _schemas, models as _models
from sqlalchemy import and_

def create_db():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db = _db.session()
    try:
        yield db
    finally:
        db.close()

def get_businessScores(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.BusinessScore).offset(skip).limit(limit).all()

def get_businesses(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Business).offset(skip).limit(limit).all()

def get_unscoredBusinesses(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Business).filter(_models.Business.scored==0).offset(skip).limit(limit).all()

def get_review_of_business(db: _orm.Session, business_id: int):
    revs = db.query(_models.Review).filter(_models.Review.business_id == business_id).all()
    reviews = []
    for rev in revs:
        user = db.query(_models.User).filter(_models.User.id == rev.user_id).first()
        business = db.query(_models.Business).filter(_models.Business.id == rev.business_id).first()
        temp = _schemas.Review(user_id = rev.user_id,content = rev.content,business_id = rev.business_id,reply_of = rev.reply_of,id = rev.id,date_created = rev.date_created,user_name = user.name, business_name = business.name)
        reviews.append(temp)
    return reviews

def get_score_of_business(db: _orm.Session, business_id: int):
    return db.query(_models.Score).filter(_models.Score.business_id == business_id).all()

def get_business(db:_orm.Session, business_id: int):
    return db.query(_models.Business).filter(_models.Business.id == business_id).first()

def delete_business(db:_orm.Session, id: int):
    db.query(_models.Score).filter(_models.Score.business_id == id).delete()
    db.query(_models.Review).filter(_models.Review.business_id == id).delete()
    db.query(_models.Business).filter(_models.Business.id == id).delete()
    user = db.query(_models.User).filter(_models.User.business_id == id).first()
    if(user):
        user.business_id = None
    db.commit()
    return {"Deleted":True}

def create_business(db:_orm.Session, business: _schemas.BusinessCreate):
    biz = _models.Business(**business.dict(),scored = False)
    db.add(biz)
    db.commit()
    db.refresh(biz)
    return biz

def create_score(db:_orm.Session, score: _schemas.ScoreCreate):
    scores = db.query(_models.Score).filter(and_(_models.Score.business_id == score.business_id, _models.Score.latest == 1)).first()
    if(scores):    
        scores.latest = 0
    s = _models.Score(**score.dict())
    db.add(s)
    b = db.query(_models.Business).filter(_models.Business.id == score.business_id).first()
    b.scored = 1;
    db.commit()
    return score

def delete_score(db:_orm.Session, score: _schemas.ScoreDelete):
    db.query(_models.Score).filter(and_(_models.Score.business_id == score.business_id, _models.Score.dateOfScore == score.dateOfScore)).delete()
    return {"Score "+str(score.business_id):"deleted."}

def create_user(db: _orm.Session, user: _schemas.UserCreate):
    db_user = _models.User(name = user.name, email = user.email, priority = user.priority, id = user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: _orm.Session, user_id: str):
    return db.query(_models.User).filter(_models.User.id == user_id).first()
    
def update_user(db: _orm.Session, user: _schemas.UserUpdate, id: str):
    db_user = db.query(_models.User).filter(_models.User.id == id).first()
    db_user.business_id = user.business_id
    db_user.name = user.name
    db_user.priority = user.priority
    db.commit()
    return user

def delete_user(db: _orm.Session, id: str):
    db.query(_models.Review).filter(_models.Review.user_id == id).delete()
    user = db.query(_models.User).filter(_models.User.id == id).delete()
    db.commit()
    return user

def create_review(db= _orm.Session, review = _schemas.createReview):
    rev = _models.Review(**review.dict())
    db.add(rev)
    db.commit()
    return rev

def delete_review(db= _orm.Session, review_id = int):
    db.query(_models.Review).filter(_models.Review.id == review_id).delete()
    db.query(_models.Review).filter(_models.Review.reply_of == review_id).delete()
    db.commit()
    return {"Review "+str(review_id): "deleted"}

def get_userProfile(db= _orm.Session, user_id = str):
    user = db.query(_models.User).filter(_models.User.id == user_id).first()
    revs = db.query(_models.Review).filter(_models.Review.user_id == user_id).all()

    reviews = []
    for rev in revs:
        user = db.query(_models.User).filter(_models.User.id == rev.user_id).first()
        business = db.query(_models.Business).filter(_models.Business.id == rev.business_id).first()
        temp = _schemas.Review(user_id = rev.user_id,content = rev.content,business_id = rev.business_id,reply_of = rev.reply_of,id = rev.id,date_created = rev.date_created,user_name = user.name, business_name = business.name)
        reviews.append(temp)

    response = _schemas.UserReviews(id=user.id,name=user.name,email=user.email,priority=user.priority,reviews=reviews)
    return response

def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.User).offset(skip).limit(limit).all()
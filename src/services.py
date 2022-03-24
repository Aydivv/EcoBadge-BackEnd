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
    return db.query(_models.Review).filter(_models.Review.business_id == business_id).all()

def get_score_of_business(db: _orm.Session, business_id: int):
    return db.query(_models.Score).filter(_models.Score.business_id == business_id).all()

def get_business(db:_orm.Session, business_id: int):
    return db.query(_models.Business).filter(_models.Business.id == business_id).first()

def delete_business(db:_orm.Session, id: int):
    db.query(_models.Business).filter(_models.Business.id == id).delete()
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



def create_user(db: _orm.Session, user: _schemas.UserCreate):
    db_user = _models.User(name = user.name, email = user.email, priority = user.priority, id = user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def create_review(db: _orm.Session, review: _schemas.createReview):
#     db_review = _models.Review(content = review.content, user_id = review.user_id, business_id = review.business_id)
#     db.add(db_review)
#     db.commit()
#     db.refresh(db_review)
#     return db_review


def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.User).offset(skip).limit(limit).all()
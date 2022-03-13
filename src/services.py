import database as _db
import sqlalchemy.orm as _orm
import schemas as _schemas, models as _models

def create_db():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db = _db.session();
    try:
        yield db
    finally:
        db.close()

def create_user(db: _orm.Session, user: _schemas.UserCreate):
    db_user = _models.User(name = user.name, email = user.email, priority = user.priority, id = user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
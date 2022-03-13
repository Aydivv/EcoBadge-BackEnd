import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas, models as _models


app = _fastapi.FastAPI()

@app.post("/users/",response_model=_schemas.User)
def create_user(user: _schemas.UserCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.create_user(db=db, user=user)


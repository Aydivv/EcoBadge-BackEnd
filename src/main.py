import email
from unicodedata import name
import fastapi as fastapi
from sqlalchemy import desc
import sqlalchemy.orm as orm
import services
import schemas
import models
from typing import List
import uvicorn



app = fastapi.FastAPI()

@app.get("/businesses",response_model=List[schemas.BusinessScore])
def get_businesses(
    skip: int = 0,
    limit: int = 10,
    db: orm.Session = fastapi.Depends(services.get_db)
):
    businesses = services.get_businessScores(db=db, skip=skip, limit=limit)
    return businesses

@app.get("/business/{business_id}",response_model=schemas.BusinessProfile)
def get_businessProfile(
    business_id: int,
    db: orm.Session = fastapi.Depends(services.get_db)
):
    b = services.get_business(db=db,business_id=business_id)
    reviews = services.get_review_of_business(db=db,business_id=business_id)
    scores = services.get_score_of_business(db=db,business_id=business_id)

    response = schemas.BusinessProfile(id=b.id,name=b.name,address=b.address,postcode=b.postcode,description=b.description,cuisine=b.cuisine,number=b.pNumber,email=b.pNumber,website=b.website,reviews=reviews,scores=scores)
    return response

@app.post("/business",response_model=schemas.BusinessCreate)
def add_business(
    business: schemas.BusinessCreate,
    db: orm.Session=fastapi.Depends(services.get_db)
):
    return services.create_business(db=db,business=business)

@app.post("/users/",response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.create_user(db=db, user=user)




@app.get("/users",response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: orm.Session = fastapi.Depends(services.get_db),
):
    users = services.get_users(db=db, skip=skip, limit=limit)
    
    return users

@app.get("/scores",response_model=List[schemas.Score])
def read_scores(
    skip: int = 0,
    limit: int = 10,
    db: orm.Session = fastapi.Depends(services.get_db),
):
    scores = services.get_scores(db=db, skip=skip, limit=limit)
    
    return scores


@app.post("/reviews/",response_model=schemas.Review)
def create_review(review: schemas.createReview, db: orm.Session =fastapi.Depends(services.get_db)):
    return services.create_review(db=db, review=review)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

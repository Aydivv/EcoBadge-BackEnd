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
import starlette.responses as _responses
from fastapi.middleware.cors import CORSMiddleware

#Get Businesses (with score) !!
#Get Unscored businesses!!
#Get Business Profile (with scores)!!

#Create Business!!
#Delete Business!!

#Create score(Update score to latest, others to not. change business to scored)!!
#Delete score

#Create user(with pic_path)!!
#Delete User!!

#Create review!!
#Reply to review!!
#Delete review!!
#User profile with reviews!!
#Get User

app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","DELETE","PUT"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return _responses.RedirectResponse("/docs")

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

    response = schemas.BusinessProfile(id=b.id,name=b.name,address=b.address,postcode=b.postcode,description=b.description,cuisine=b.cuisine,number=b.pNumber,email=b.email,website=b.website,reviews=reviews,scores=scores)
    return response

@app.get("/unscored",response_model=List[schemas.UnscoredBusiness])
def get_unscoredBusinesses(
    skip: int = 0,
    limit: int = 10,
    db: orm.Session = fastapi.Depends(services.get_db)):
    businesses = services.get_unscoredBusinesses(db=db,skip=skip,limit=limit)
    return businesses

@app.get("/recent", response_model=schemas.UnscoredBusiness)
def getRecentbusiness(
    db: orm.Session = fastapi.Depends(services.get_db)
):
    return services.get_recentBusiness(db=db)

@app.post("/business",response_model=schemas.BusinessCreate)
def add_business(
    business: schemas.BusinessCreate,
    db: orm.Session=fastapi.Depends(services.get_db)
):
    return services.create_business(db=db,business=business)

@app.delete("/business/{business_id}")
def delete_business(business_id: int,db: orm.Session = fastapi.Depends(services.get_db) ):
    return services.delete_business(db=db,id=business_id)

@app.put("/business/{business_id}",response_model=schemas.BusinessCreate)
def update_business(business: schemas.BusinessCreate, id: int, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.update_business(db=db,id=id,business=business)

@app.post('/score',response_model=schemas.ScoreCreate)
def create_score(score: schemas.ScoreCreate, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.create_score(db=db,score=score)

@app.delete('/score')
def delete_score(score: schemas.ScoreDelete, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.delete_score(db=db,score=score)

@app.post("/users/",response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.create_user(db=db, user=user)

@app.get("/users/{id}",response_model=schemas.User)
def get_user(id: str, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.get_user(db=db,user_id=id)

@app.delete("/users/{id}")
def delete_user(id: str, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.delete_user(db=db,id=id)

@app.put("/users/{id}")
def update_user(user: schemas.UserUpdate, id: str, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.update_user(db=db,user=user,id=id)

@app.post("/review",response_model=schemas.Review)
def create_review(rev: schemas.createReview, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.create_review(db=db,review = rev)

@app.delete("/review/{id}")
def delete_review(id: int, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.delete_review(db=db,review_id = id)

@app.get("/userProfile/{id}",response_model=schemas.UserReviews)
def get_userProfile(id: str, db: orm.Session=fastapi.Depends(services.get_db)):
    return services.get_userProfile(db=db,user_id= id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

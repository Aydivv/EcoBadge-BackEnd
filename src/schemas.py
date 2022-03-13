from typing import List
import pydantic as _pydantic
import datetime as _dt

class ReviewBase(_pydantic.BaseModel):
    user_id: str
    business_id: int
    content: str

class createReview(ReviewBase):
    pass

class Review(ReviewBase):
    user_name: str
    date_created: _dt.datetime
    class Config:
        orm_mode = True

class UserBase(_pydantic.BaseModel):
    name: str
    email: str
    priority: int

class UserCreate(UserBase):
    id: str

class User(UserBase):
    class Config:
        orm_mode = True
    pass

class UserReviews(UserBase):
    reviews: List[Review] = []
    class Config:
        orm_mode = True
    pass

class ScoreBase(_pydantic.BaseModel):
    score: int
    business_id: int
    vegan: bool
    singleUsePlastic: bool
    foodwasteCollection: bool
    localProduce: bool

class ScoreCreate(ScoreBase):
    latest = True

class Score(ScoreBase):
    dateOfScore: _dt.datetime
    class Config:
        orm_mode = True

class BusinessBase(_pydantic.BaseModel):
    name: str
    address: str
    postcode: str
    desc: str
    cuisine: str
    scored: bool

class BusinessCreate(BusinessBase):
    number: str
    email: str
    website: str
    pass

class Business(BusinessBase):
    score: int
    class Config:
        orm_mode = True

class BusinessProfile(BusinessBase):
    scores: List[Score] = []
    number: str
    email: str
    website: str
    reviews: List[Review] = []
    class Config:
        orm_mode = True

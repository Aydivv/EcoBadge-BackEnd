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
    business_id: int
    score: int
    vegan: bool
    singleUsePlastic: bool
    foodwasteCollection: bool
    localProduce: bool
    price: int

class ScoreCreate(ScoreBase):
    latest = True
    class Config:
        orm_mode = True

class Score(ScoreBase):
    latest: bool
    dateOfScore: _dt.datetime
    class Config:
        orm_mode = True

class BusinessScore(_pydantic.BaseModel):
    business_id: int
    name: str
    address: str
    postcode: str
    description: str
    cuisine: str
    score: int
    vegan: bool
    singleUsePlastic: bool
    foodwasteCollection: bool
    localProduce: bool
    price: int
    class Config:
        orm_mode = True

class UnscoredBusiness(_pydantic.BaseModel):
    id: int
    name: str
    address: str
    postcode: str
    description: str
    cuisine: str
    class Config:
        orm_mode = True

class BusinessProfile(_pydantic.BaseModel):
    id: int
    name: str
    address: str
    postcode: str
    description: str
    cuisine: str
    number: str
    email: str
    website: str
    scores: List[Score]
    reviews: List[Review]
    class Config:
        orm_mode = True
    
class BusinessCreate(_pydantic.BaseModel):
    name: str
    address: str
    postcode: str
    pNumber: str
    email: str
    description: str
    website: str
    cuisine: str
    class Config:
        orm_mode = True
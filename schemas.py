from typing import List, Optional
import pydantic as _pydantic
import datetime as _dt

class ReviewBase(_pydantic.BaseModel):
    user_id: str
    business_id: int
    content: str
    reply_of: int = None

class createReview(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    date_created: _dt.datetime
    user_name: Optional[str] = None
    business_name: Optional[str] = None
    class Config:
        orm_mode = True

class UserBase(_pydantic.BaseModel):
    name: str
    priority: int
    

class UserCreate(UserBase):
    id: str
    email: str
    pass

class User(UserBase):
    id: str
    email: str
    business_id: Optional[int] = None
    class Config:
        orm_mode = True
    pass

class UserUpdate(UserBase):
    class Config:
        orm_mode = True
    business_id: Optional[int] = None

class UserReviews(UserBase):
    id: str
    email: str
    business_id: Optional[int] = None
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

class ScoreDelete(_pydantic.BaseModel):
    business_id: int
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
    uber: Optional[str] = None
    justeat: Optional[str] = None
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
    uber: Optional[str] = None
    justeat: Optional[str] = None
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
    uber: Optional[str] = None
    justeat: Optional[str] = None
    class Config:
        orm_mode = True
from pydantic import BaseModel

class Userinfo(BaseModel):
    name: str
    userid: str
    password: str
    email:str

class User(BaseModel):
    userid: str
    password: str

class Userid(BaseModel):
    userid: str
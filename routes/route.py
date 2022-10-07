from copyreg import constructor
from distutils.command.config import config
from typing import Collection
from unittest import result
from fastapi import APIRouter,Header
from config import db
from typing import Union
from models.todo import Todo
from models.user import Userinfo,User,Userid
router = APIRouter()

## db 관려 함수 사용 따로 분리 필요
##  auto increase num 으로 구분 짓고싶음
## 수정하면 수정한 날짜로 업데이트 되게 변경
## title은 겹칠수도 있는데 no가 안겹치게 
## 현재는 title 중점으로 만들었음



#DEF: login/join/logout
#bcrypt 나중에 추가
@router.post("/join")
async def createUser(user:Userinfo):
    x = db.createUser(dict(user))
    if(x==False):
        return {"msg":"already exist"}
    return {"msg":"succeed"}

@router.post("/login")
async def loginUser(user:User):
    x = db.loginUser(dict(user))
    if(x== False):
        return {"msg":"login Fail"}
    else:
        print(x)
        return {"msg":"succeed",
                "userid":x['userid'],
                "name":x['name']}

#DEF: todo
@router.post("/todo")
async def createTodo(todo:Todo):
    x = db.createTodo(dict(todo))
    #x.inserted_id
    return {'msg':'succeed'};

@router.post("/todo/{userid}")
async def createTodo(userid:str, todo:Todo):
    x = db.createTodo(userid, dict(todo))
    #x.inserted_id
    return {'msg':'succeed'};

@router.get("/todo/{userid}")
async def readTodo(userid:str):
    print("userid",userid)
    res_array = db.lookupTodo(userid)
    return res_array

    
@router.get("/todo")
async def readAllTodo():
    res_array= db.lookupTodos()
    return res_array

@router.put("/todo/{contents}")
async def updateTodo(contents:str,todo:Todo):
    x = db.updateTodo({"contents":contents},{"$set":dict(todo)})
    return {"msg":"succeed update"}


@router.delete("/todo/{contents}")
async def deleteTodo(contents:str):
    x = db.deleteTodo({"contents":contents})
    return {"msg":"succeed del"}

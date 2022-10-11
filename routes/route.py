from typing import Collection, Optional
from unittest import result
from fastapi import APIRouter,Request
from typing import Union
from models.todo import Todo
from models.user import Userinfo,User,Userid
from config import tododb
from config import userdb
from config import token
router = APIRouter()

## db 관려 함수 사용 따로 분리 필요
##  auto increase num 으로 구분 짓고싶음
## 수정하면 수정한 날짜로 업데이트 되게 변경
## title은 겹칠수도 있는데 no가 안겹치게 
## 현재는 title 중점으로 만들었음

@router.get("/auth")
async def authToken(myToken:str):
    token.authToken({"token":myToken})

    # TRUE FALSE 로 인증 확인 
    # 인증 메커니즘은 일단 유효성 판별 > 이후 DB 에 있는 token이랑 판별
    # DB 에 있는 token과 같을시 return


#DEF: login/join/logout
#bcrypt 나중에 추가
@router.post("/join")
async def createUser(user:Userinfo):
    x = userdb.createUser(dict(user))
    if(x==False):
        return {"msg":"already exist"}
    return {"msg":"succeed"}

@router.post("/login")
async def loginUser(user:User):
    x = userdb.loginUser(dict(user))
    if(x['state']== False):
        return {"msg":x}
    else:
        print(x)
        return {"msg":"succeed",
            "token":x["token"]}

#DEF: todo
@router.post("/todo")
async def createTodo(todo:Todo, req:Request):
    accessToken = req.headers["Authorization"]
    x = tododb.createTodo(accessToken, dict(todo))
    #x.inserted_id
    print(x)
    return x

@router.post("/todo/{userid}")
async def createTodo(userid:str, todo:Todo):
    x = tododb.createTodo(userid, dict(todo))
    #x.inserted_id
    return {'msg':'succeed'};

@router.get("/todo/{userid}")
async def readTodo(userid:str):
    print("userid",userid)
    res_array = tododb.lookupTodo(userid)
    return res_array

    
@router.get("/todo")
async def readAllTodo(req:Request):
    accessToken = req.headers["Authorization"]
    res_array= tododb.lookupTodo(accessToken)
    return res_array

@router.put("/todo/{contents}")
async def updateTodo(contents:str,todo:Todo):
    x = tododb.updateTodo({"contents":contents},{"$set":dict(todo)})
    return {"msg":"succeed update"}


@router.delete("/todo/{contents}")
async def deleteTodo(contents:str, req:Request):
    accessToken = req.headers["Authorization"]
    x = tododb.deleteTodo(accessToken,{"contents":contents})
    return x

from distutils.command.config import config
from typing import Collection
from unittest import result
from fastapi import APIRouter
from config import db
from models.todo import Todo
router = APIRouter()

## db 관려 함수 사용 따로 분리 필요
##  auto increase num 으로 구분 짓고싶음
## 수정하면 수정한 날짜로 업데이트 되게 변경
## title은 겹칠수도 있는데 no가 안겹치게 
## 현재는 title 중점으로 만들었음



#login/join/logout


#todo
@router.post("/todo")
async def createTodo(todo:Todo):
    x = db.createTodo(dict(todo))
    #x.inserted_id
    return {'msg':'succeed'};

@router.get("/todo/{title}")
async def readTodo(title:str):
    res = db.lookupTodo(dict({"title":title}))
    return res

    
@router.get("/todo")
async def readAllTodo():
    res_array= db.lookupTodos()
    return res_array

@router.put("/todo/{title}")
async def updateTodo(title:str,todo:Todo):
    x = db.updateTodo({"title":title},{"$set":dict(todo)})
    return {"msg":"succeed update"}


@router.delete("/todo/{title}")
async def deleteTodo(title:str):
    x = db.deleteTodo({"title":title})
    return {"msg":"succeed del"}

from distutils.command.config import config
from typing import Collection
from unittest import result
from fastapi import APIRouter
from config.db import conn
from models.todo import Todo
from datetime import datetime
router = APIRouter()
db = conn.fastapi.todo

## db 관려 함수 사용 따로 분리 필요
##  auto increase num 으로 구분 짓고싶음
## 수정하면 수정한 날짜로 업데이트 되게 변경
## title은 겹칠수도 있는데 no가 안겹치게 
## 현재는 title 중점으로 만들었음
@router.post("/todo")
async def createTodo(todo:Todo):
    print(todo)
    today = datetime.today()
    resValue = dict(todo) 
    resValue["date"] =today
    print(resValue)
    results =db.insert_one(resValue)
    return "insert";


@router.get("/todo/{title}")
async def readTodo(title:str):
    result = db.find_one(dict({"title":title}))
    resValue = {"title":result['title'],"contents":result['contents'],"date":result['date']}
    return resValue

    
@router.get("/todo")
async def readAllTodo():
    results = db.find()
    resValue = []
    for s in results:
        print(s)
        resValue.append({"title":s['title'],"contents":s['contents'],"date":s['date']})
    return resValue

@router.put("/todo/{title}")
async def updateTodo(title:str,todo:Todo):
    print(todo)
    result = db.update_one({"title":title},{"$set":dict(todo)})
    print(result)
    return {"msg":"good"}


@router.delete("/todo/{title}")
async def deleteTodo(title:str):
    result = db.delete_one({"title":title})
    print(result)
    return {"msg":"good"}

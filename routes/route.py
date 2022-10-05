from distutils.command.config import config
from typing import Collection
from fastapi import APIRouter
from config.db import conn
from models.todo import Todo
router = APIRouter()
db = conn.fastapi.todo

@router.post("/todo")
async def createTodo(todo:Todo):
    #print(todo)
    results =db.insert_one(dict(todo))
    return "insert";


@router.get("/todo/{no}")
async def readTodo(id:str):
    result = db.find_one(dict({"title":id}))
    resValue = {"title":result['title'],"contents":result['contents']}
    return resValue

    
@router.get("/todo")
async def readAllTodo():
    results = db.find()
    resValue = []
    for s in results:
        print(s)
        resValue.append({"title":s['title'],"contents":s['contents']})
    return resValue
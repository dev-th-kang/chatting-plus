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
    return {"id":id}

    
@router.get("/todo")
async def readAllTodo():
    return 0
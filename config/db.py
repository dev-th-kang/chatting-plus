from unittest import result
from pymongo import MongoClient
from datetime import datetime
mongo_url = "mongodb://root:Kk2001devth@127.0.0.1:27017/"
conn = MongoClient(mongo_url)
#db = todo_query
todo_query = conn.fastapi.todo
'''
#사용자 관련
def createUser(user):
    
def deleteUser(user):

def updateUser(user):

def lookupUser(user):

def lookupUsers():
'''

# toDo list
def createTodo(todo):
    res = dict(todo)
    res["date"] = datetime.today()
    res =todo_query.insert_one(res)
    return res

def deleteTodo(title):
    res = todo_query.delete_one(title)
    return res

def updateTodo(filter,set):
    res= todo_query.update_one(filter,set)
    return res

def lookupTodo(title):
    results = todo_query.find_one(title)
    res = {"title":results['title'],"contents":results['contents'],"date":results['date']}
    return res

def lookupTodos():
    results = todo_query.find()
    res = []
    for s in results:
        res.append({"title":s['title'],"contents":s['contents'],"date":s['date']})
    return res
#"mongodb://localhost:27017/test"

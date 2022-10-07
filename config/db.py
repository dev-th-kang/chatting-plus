from asyncio.windows_events import NULL
from copyreg import constructor
from unittest import result
from pymongo import MongoClient
from datetime import datetime
mongo_url = "mongodb://root:Kk2001devth@127.0.0.1:27017/"
conn = MongoClient(mongo_url)
#db = todo_query
todo_query = conn.fastapi.todo

#사용자 관련
def createUser(userinfo):
    user_query = conn.fastapi.memberlist
    rows = user_query.find_one({"userid":userinfo["userid"]})
    if(rows!=None):
        return False
    
    res = user_query.insert_one(userinfo)
    return res

def loginUser(user):
    user_query = conn.fastapi.memberlist
    rows = user_query.find_one(user)
    if(rows==None):
        return False
    return rows
'''
def deleteUser(user):

def updateUser(user):

def lookupUser(user):

def lookupUsers():
'''

# toDo list
def createTodo(userid,todo):
    print('userid',userid);
    board_query = conn.fastapi["todo_"+userid];
    res = dict(todo)
    res["date"] = datetime.today()
    res =board_query.insert_one(res)
    return res

def deleteTodo(contents):
    res = todo_query.delete_one(contents)
    return res

def updateTodo(filter,set):
    res= todo_query.update_one(filter,set)
    return res

def lookupTodo(userid):
    
    board_query = conn.fastapi["todo_"+userid];
    results = board_query.find()
    res = []
    for s in results:
        res.append({"contents":s['contents'],"date":s['date']})
    return res

def lookupTodos():
    results = todo_query.find()
    res = []
    for s in results:
        res.append({"contents":s['contents'],"date":s['date']})
    return res
#"mongodb://localhost:27017/test"

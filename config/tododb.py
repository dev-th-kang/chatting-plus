from datetime import datetime
from config.db import conn
# toDo list
todo_query = conn.fastapi.todo
def createTodo(userid,todo):
    print('userid',userid);
    board_query = conn.fastapi["todo_"+userid];
    res = dict(todo)
    res["date"] = datetime.today()
    res =board_query.insert_one(res)
    return res

def deleteTodo(userid,contents):
    board_query = conn.fastapi["todo_"+userid];
    print(board_query)
    res = board_query.delete_one(contents)
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
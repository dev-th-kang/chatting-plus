from datetime import datetime
from config.db import conn
from config.token import authToken
# toDo list
todo_query = conn.fastapi.todo
def createTodo(token,todo):
    #id 검색
    results = authToken(token)
    print(results)
    if "token" in results:
        return results
    else:
        #print("todo_"+results['userid'])
        board_query = conn.fastapi["todo_"+results['userid']];
        res = dict(todo)
        res["date"] = datetime.today()
        board_query.insert_one(res)
        return {"state":True}

def deleteTodo(token,contents):
    results = authToken(token)
    if "token" in results:
        return results
    else:
        board_query = conn.fastapi["todo_"+results['userid']];
        print(board_query)
        board_query.delete_one(contents)
        return {"state":True}

def updateTodo(filter,set):
    res= todo_query.update_one(filter,set)
    return res

def lookupTodo(token):
    results = authToken(token)

    if "token" in results:
        return results
    else:
        board_query = conn.fastapi["todo_"+results['userid']];
        results = board_query.find()
        res = []
        for s in results:
            res.append({"contents":s['contents'],"date":s['date']})
        return res

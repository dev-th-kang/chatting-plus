from datetime import datetime
from config.db import conn
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
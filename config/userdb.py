import bcrypt
from datetime import datetime
from config.db import conn
from config.token import issuranceAccessToken, authToken
#사용자 관련
def createUser(userinfo):
    user_query = conn.fastapi.memberlist
    rows = user_query.find_one({"userid":userinfo["userid"]})
    # 겹치는 아이디가 있으면 False Return
    if(rows!=None):
        return False
    pw = userinfo['password']
    hashed_password = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    userinfo['password'] = hashed_password
    res = user_query.insert_one(userinfo)
    return res

def loginUser(user):
    userid = user["userid"]
    userpw = user["password"]
    user_query = conn.fastapi.memberlist

    # ID 일치 여부 판별
    rows = user_query.find_one({"userid":userid})
    if(rows==None):
        return {'state':False,'msg': 'id not existing'}
    # 비밀번호 일치 여부 판별
    if(bcrypt.checkpw(userpw.encode('utf-8'), rows['password']) == True):
        accessToken = issuranceAccessToken(user)
        return {'state':True,'msg':'succeed','token':accessToken}
    else:
        return {'state':False,'msg': 'pw isnt corrent'};

def logoutUser(token):
    user_query = conn.fastapi.user_token
    rows = user_query.delete_one({"token":token})
    if(rows== None):
        return {"msg":"error"}
    else:
        return {"msg":"succeed"}
'''
def deleteUser(user):

def updateUser(user):

def lookupUser(user):

def lookupUsers():
'''
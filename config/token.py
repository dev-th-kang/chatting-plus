
import jwt
from datetime import datetime, timedelta
import time
from config.db import conn
def issuranceAccessToken(user):
    
    member_query = conn.fastapi.memberlist
    rows = member_query.find_one({'userid':user['userid']})
    #print("asdasd",rows)
    payload = {
        'userid':rows['userid'],
        'name':rows['name'],
        'exp':time.time() + 10
    }
    print(payload)
    accessToken = jwt.encode(payload,'secret',algorithm='HS256')
    userToken_query = conn.fastapi.user_token
    userToken_query.update_one({'userid':user['userid']}, {"$set":{'userid':user['userid'],'token':accessToken}}, upsert=True)
    return {"token":accessToken}

def authToken(token):
    userToken_query = conn.fastapi.user_token
    rows = userToken_query.find_one({"token":token})
    print(rows)
    if(rows != None):
        try:
            decode_data = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(decode_data['exp'])
            print(time.time())
            return decode_data
        except jwt.ExpiredSignatureError:
            # expire!
            print(rows)
            return issuranceAccessToken({"userid":rows['userid']})


    return {"state":False}
# def authToken():


#myToken = issuranceAccessToken({"userid":"cake16290", "username":"1234"})
#authToken({"token":myToken})
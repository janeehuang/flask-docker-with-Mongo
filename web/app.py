from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os

from pymongo import MongoClient


app  = Flask(__name__)
api  = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    'num_of_users' : 0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]["num_of_users"]
        new_num = prev_num + 1
        UserNum.update_one({},{"$set":{"num_of_users" : new_num}})
        return str("Hello user " + str(new_num))


def checkPostedData(postedData, funcName):
    if (funcName == "add" or funcName == "subtract" or funcName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301 #missing parameter
        else:
            return 200
    elif (funcName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301 #missing parameter
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200



class Add(Resource):
    def post(self):
        #If I am here, then the resource Add was requested using the Method Post

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = checkPostedData(postedData,"add")
        if (status_code != 200):
            retJson = {
                "Message" : "An error happened",
                "Status Code" : status_code
            }
            return retJson

        #If I am here, the status_code=200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Add posted data:
        ret = x+y
        retMap = {
            "Message" : ret,
            "Status code" : 200
        }
        return retMap


class Subtract(Resource):
    def post(self):
        #If I am here, then the resource Subtract was requested using the Method Post

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = checkPostedData(postedData,"subtract")
        if (status_code != 200):
            retJson = {
                "Message" : "An error happened",
                "Status Code" : status_code
            }
            return retJson

        #If I am here, the status_code=200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Subtract posted data:
        ret = x-y
        retMap = {
            "Message" : ret,
            "Status code" : 200
        }
        return retMap

class Multiply(Resource):
    def post(self):
        #If I am here, then the resource Multiply was requested using the Method Post

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = checkPostedData(postedData,"multiply")
        if (status_code != 200):
            retJson = {
                "Message" : "An error happened",
                "Status Code" : status_code
            }
            return retJson

        #If I am here, the status_code=200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Multiply posted data:
        ret = x*y
        retMap = {
            "Message" : ret,
            "Status code" : 200
        }
        return retMap

class Divide(Resource):
    def post(self):
        #If I am here, then the resource Divide was requested using the Method Post

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify Validity of posted data
        status_code = checkPostedData(postedData,"division")
        if (status_code != 200):
            retJson = {
                "Message" : "An error happened",
                "Status Code" : status_code
            }
            return retJson

        #If I am here, the status_code=200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Divide posted data:
        ret = x/y
        retMap = {
            "Message" : ret,
            "Status code" : 200
        }
        return retMap

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/division")
api.add_resource(Visit,"/visit")



@app.route("/")
def hello_world():
    return "Hello World!"




if __name__ == "__main__":
    app.run("0.0.0.0")
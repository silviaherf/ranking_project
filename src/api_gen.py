import os
from dotenv import load_dotenv
load_dotenv()
import requests
from flask import Flask
from flask import request, Response
import re
from src.database import db
import src.data_exportation as export
import json
from bson.json_util import dumps

app = Flask("ranking")

@app.route("/student/create")
@app.route("/student/create/<studentname>")
def createStudent(studentname=None):
    params=dict(request.args)
    student={"name": studentname,**params}
    if not studentname:
        return {
            "status": "error",
            "message": "Any student in query , please specify one"
        }, 400
    if db.students.find_one({"name": studentname}):
        db.students.update_one({"name": studentname},{"$set":student})
        return 'This student is already on MongoDB'
    else:
        print(student)
        stu=export.student_toMongo(student)
        return dumps({"_id": stu.inserted_id})
        


@app.route("/student/all")
def allStudents():

    cursor=db.students.find({"_id":{'$exists':True}},{'lab':0, 'pull_request':0})

    return dumps(list(cursor))



@app.route("/lab/create/<lab_prefix>")
def searchLab(lab_prefix):
    if not lab_prefix:
        return {
            "status": "error",
            "message": "Any lab-prefix in query , please specify one"
        }, 400

    if db.labs.find_one({"lab_prefix": lab_prefix}):
        return 'This lab is already on MongoDB'
    else:
        labs=export.lab_toMongo(lab)
        return {"_id": labs.inserted_id}
"""

(GET) /lab/<lab_id>/search
Purpose: Search student submissions on specific lab
Params: user_id
Returns: See Lab analysis section

"""
"""

@app.route("/lab/<lab_id>/search")
#@asJsonResponse
def searchLab(lab-prefix):
    
    if not lab-prefix:
        # Set status code to 400 BAD REQUEST
        return {
            "status": "error",
            "message": "Any student in query , please specify one"
        }, 400

    # Search a company in mongodb database
    projection = {"name": 1, "category_code": 1,"description":1}
    searchRE = re.compile(f"{companyNameQuery}", re.IGNORECASE)
    foundStudent = db["crunchbase"].find_one(
        {"name": searchRE}, projection)

    if not foundStudent:
        # Set status code to 404 NOT FOUND
        return {
            "status": "not found",
            "message": f"No student found with name {foundStudent} in database"
        }, 404

    return {
        "status": "OK",
        "searchQuery": lab-prefix,
        "student": foundStudent
    }

"""
"""

(GET) /lab/memeranking
Purpose: Ranking of the most used memes for datamad0820 divided by labs
"""

"""

@app.route("/lab/memeranking")
#@asJsonResponse
def searchLab(lab-prefix):
    
    if not lab-prefix:
        # Set status code to 400 BAD REQUEST
        return {
            "status": "error",
            "message": "Any student in query , please specify one"
        }, 400

    # Search a company in mongodb database
    projection = {"name": 1, "category_code": 1,"description":1}
    searchRE = re.compile(f"{companyNameQuery}", re.IGNORECASE)
    foundStudent = db["crunchbase"].find_one(
        {"name": searchRE}, projection)

    if not foundStudent:
        # Set status code to 404 NOT FOUND
        return {
            "status": "not found",
            "message": f"No student found with name {foundStudent} in database"
        }, 404

    return {
        "status": "OK",
        "searchQuery": lab-prefix,
        "student": foundStudent
    }

"""

"""
(GET) /lab/<lab_id>/meme
Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.


"""
"""

@app.route("/lab/<lab_id>/meme")
#@asJsonResponse
def searchLab(lab-prefix):
    
    if not lab-prefix:
        # Set status code to 400 BAD REQUEST
        return {
            "status": "error",
            "message": "Any student in query , please specify one"
        }, 400

    # Search a company in mongodb database
    projection = {"name": 1, "category_code": 1,"description":1}
    searchRE = re.compile(f"{companyNameQuery}", re.IGNORECASE)
    foundStudent = db["crunchbase"].find_one(
        {"name": searchRE}, projection)

    if not foundStudent:
        # Set status code to 404 NOT FOUND
        return {
            "status": "not found",
            "message": f"No student found with name {foundStudent} in database"
        }, 404

    return {
        "status": "OK",
        "searchQuery": lab-prefix,
        "student": foundStudent
    }

"""


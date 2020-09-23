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
    """
    Purpose: Create a student and save into DB
    Params: studentname the student name
    Returns: student_id
    """
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
        stu=export.student_toMongo(student)
        return dumps({"_id": stu.inserted_id})
        


@app.route("/student/all")
def allStudents():
    """
    Purpose: List all students in database
    Returns: An array of student objects
    """
    cursor=db.students.distinct("name") 

    return dumps(list(cursor))


#Pendiente cambiar lab-prefix por lab
@app.route("/lab/create")
@app.route("/lab/create/<lab_prefix>")
def searchLab(lab_prefix):
    params=dict(request.args)
    lab={"name": lab_prefix,**params}
    if not lab_prefix:
        return {
            "status": "error",
            "message": "Any lab-prefix in query , please specify one"
        }, 400

    if db.labs.find_one({"lab_prefix": lab_prefix}):
        return 'This lab is already on MongoDB'
    else:
        labs=export.lab_toMongo(lab)
        return dumps({"_id": labs.inserted_id})



@app.route("/lab/<lab_id>/search")
def searchLab_Student(lab_id):
    """
    Purpose: Search student submissions on specific lab
    Params: user_id
    Returns: Number of open PR
            Number of closed PR
            Percentage of completeness (closed vs open)
            List number of missing pr from students
            The list of unique memes used for that lab
            Instructor grade time in hours: (pr_close_time-last_commit_time)

"""
    user_id = request.args.get("user_id","silviaherf")
    
    projection = {"name": 1}

    result=db.students.find({'$and':[ {"name": "silviaherf"}, {"lab":lab_id}]},projection)

  
    return dumps({
        "status": "OK",
        "searchQuery": lab_id,
        "student": result
    })

"""

@app.route("/lab/memeranking")
#@asJsonResponse
def searchLab(lab_prefix):
    """
    #Purpose: Ranking of the most used memes for datamad0820 divided by labs
"""
    if not lab_prefix:
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


@app.route("/lab/<lab_id>/meme")
#@asJsonResponse
def searchLab(lab_prefix):
    """
    #Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.
"""
    
    if not lab_prefix:
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

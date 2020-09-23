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
import random

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



@app.route("/lab/create")
@app.route("/lab/create/<lab_prefix>")
def createLab(lab_prefix):
    params=dict(request.args)
    lab={"name": lab_prefix,**params}
    if not lab_prefix:
        return {
            "status": "error",
            "message": "Any lab-prefix in query , please specify one"
        }, 400

    if db.labs.find_one({"lab": lab_prefix}):
        return 'This lab is already on MongoDB'
    else:
        lab_add=export.lab_toMongo(lab)
        return dumps({"_id": lab_add.inserted_id})


"""
@app.route("/lab/<lab_prefix>/search")
def searchLab_Student(lab_prefix):
    """
"""
    Purpose: Search student submissions on specific lab
    Params: user_id
    Returns: If PR is open or closed

    """
"""
    user_id = request.args.get("user_id","silviaherf")
    
    projection = {"name": 1}

    pr=(db.students.find_one({'$and':[ {"name": user_id}, {"lab":lab_prefix}]},{"_id":0,"pull_request":1}))
    result=db.labs.find( {"pull_request": pr['pull_request']},{"_id":0,"pull_request_status":1})

  
    return dumps(result)
"""

@app.route("/lab/<lab_prefix>/search")
def searchLab(lab_prefix):
    """
    Purpose: Search student submissions on specific lab
    Params: lab_prefix
    Returns: Number of open PR
            Number of closed PR
            Percentage of completeness (closed vs open)
            List number of missing pr from students
            The list of unique memes used for that lab
            Instructor grade time in hours: (pr_close_time-last_commit_time)

"""
        
    projection = {"_id":0,"meme1": 1}
    opened_pr=db.labs.find({"$and":[{"lab":lab_prefix},{"pull_request_status": "open"}]}).count()
    closed_pr=db.labs.find({"$and":[{"lab":lab_prefix},{"pull_request_status": "closed"}]}).count()
    percentage=round(closed_pr/(opened_pr+closed_pr)*100,2)

    #pendiente comprobar para joins y comentarios
    missing_pr=db.students.find({"$and":[{"lab":lab_prefix},{"pull_request": {"$exists":False}}]}).count()

    memes=db.labs.aggregate([   
        { "$match":  {"lab": lab_prefix} }, { "$group": {" _id": "meme1" } }])
        

    
    result={'-The number of opened PR is': opened_pr,
    '-The number of closed PR is': closed_pr,
    'The percentage of complteness is': percentage,
    'Number of PR': missing_pr,
    'Distinct memes': memes
    
    }
  
    return dumps(result)






@app.route("/memeranking")
#@asJsonResponse
def memeRanking():
    """
    #Purpose: Ranking of the most used memes for datamad0820 divided by labs
"""
    #pendiente buscar memes y sustituir en match
    projection = {"_id":0, "meme1":1, "meme2":1}
    result=db.labs.aggregate([   
        { "$match":  {"meme": "meme1"} }, { "$group": { "_id": "lab"}}, {"$project":projection}])

     
    return dumps(result)



@app.route("/lab/<lab_prefix>/meme")
def randomMeme(lab_prefix):
    """
    #Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.
"""

    projection = {"_id":0, "meme1":1}
    result=db.labs.aggregate([  
        { "$sample": {"size": 1} }, 
        { "$match":  {"lab": lab_prefix} }, {"$project":projection}])
    
    return dumps(result)


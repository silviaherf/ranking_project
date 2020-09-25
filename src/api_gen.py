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
import base64


app = Flask("ranking")

@app.route("/")

    #This is just the first view of the API
   
def saludo():
  
    return dumps('Welcome to the DataMad0820 Ranking API!!!')



@app.route("/student/create")
@app.route("/student/create/<studentname>")
def createStudent(studentname=None):
    """
    Purpose: This endpoint creates a student document and saves into MongoDB students collection. It also updates a student document in MongoDB if it already exists
    Params: the student's name in Github (his nickname)
    Queryparams:  any parameter needed by the user
    Returns: the generated id for that document in MongoDB
    """
    params=dict(request.args)
    student={"name": studentname,**params}
    if not studentname:
        return {
            "status": "error",
            "message": "No student in query , please specify one"
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

    
    
    

@app.route("/lab/create", methods=['GET', 'POST']) 
def createLab():
   
    """
    This endpoint acts both with GET or POST method. For POST method, it does not work in any web browser, it must be opened with Postman or similar

       
    Purpose:  This endpoint creates a lab document and saves into MongoDB labs collection. It also updates a lab document in MongoDB if it already exists
    Params: The lab-prefix to be analyzed (its name). Example: lab-scavengers
    Returns: the generated id for that document in MongoDB
    
"""

    if request.method == 'POST':
        lab_prefix = request.form.get('lab_prefix')
        lab={"lab": lab_prefix}   
        if db.labs.find_one({"lab": lab_prefix}):
            return 'This lab is already on MongoDB'
        else:
            lab_add=export.lab_toMongo(lab)
            return dumps({"_id": lab_add.inserted_id})

    else:
        lab_prefix=request.args.get("lab_prefix")
        lab={"lab": lab_prefix}
        if not lab_prefix:
            return {
                "status": "error",
                "message": "No lab-prefix in query , please specify one"
            }, 400

        if db.labs.find_one({"lab": lab_prefix}):
            return 'This lab is already on MongoDB'
        else:
            lab_add=export.lab_toMongo(lab)
            return dumps({"_id": lab_add.inserted_id})    
        




@app.route("/lab/<lab_prefix>/search")
def searchLab(lab_prefix):
    """
    Purpose: Returns lab analysis
    Params: lab_prefix->the name of the lab we want information about. Example: lab-scavengers
    Returns: Number of open PR
            Number of closed PR
            Percentage of completeness (closed vs open)
            The number of missing PR from students
            The list of unique url of memes used for that lab
            Instructor correction time in hours

"""
        
    
    opened_pr=db.labs.find({"$and":[{"lab":lab_prefix},{"pull_request_status": "open"}]}).count()
    closed_pr=db.labs.find({"$and":[{"lab":lab_prefix},{"pull_request_status": "closed"}]}).count()
    if closed_pr!=0:
        percentage=round(closed_pr/(opened_pr+closed_pr)*100,2)
    else:
        percentage='0 closed PR, percentage cannot be calculated'

    
    missing_pr=db.students.find({"$and":[{"lab":lab_prefix},{"pull_request":{"$in":[None]}}]}).count()
    if missing_pr!=(opened_pr+closed_pr):
        join1=db.students.find({"$and":[{"lab":lab_prefix},{"join1":{"$nin":[None]}}]},{"_id":0,"join1":1})
        if len(list(join1))>0:
            missing_pr-=join1.count()
        join2=db.students.find({"$and":[{"lab":lab_prefix},{"join2":{"$nin":[None]}}]},{"_id":0,"join2":1})
        if len(list(join2))>0:
            missing_pr-=join2.count()
        
        mentioned1=db.students.find({"$and":[{"lab":lab_prefix},{"mentioned1":{"$nin":[None]}}]},{"_id":0,"mentioned1":1})
        if len(list(mentioned1))>0 and list(mentioned1)!=list(join1) and list(mentioned1)!=list(join2):
            missing_pr-=mentioned1.count()

        mentioned2=db.students.find({"$and":[{"lab":lab_prefix},{"mentioned2":{"$nin":[None]}}]},{"_id":0,"mentioned2":1})
        if len(list(mentioned2))>0 and list(mentioned2)!=list(join2) and list(mentioned2)!=list(join1):
            missing_pr-=mentioned2.count()
       
  
    
    
    meme2=db.labs.find({"$and":[{"lab":lab_prefix},{"meme2":{"$nin":[None]}}]},{"_id":0,"meme2":1}).distinct("meme2")
    
    meme1=db.labs.find({"$and":[{"lab":lab_prefix},{"meme1":{"$nin":[None]}},{"meme2":{"$in":[None]}}]},{"_id":0,"meme1":1}).distinct("meme1")
    if len(list(meme2))==0:
        memes=list(meme1)
    else:
        meme1=list(meme1)
        meme1.append(list(meme2))
        memes=meme1
   
    instructors=list(db.labs.find({'lab':lab_prefix}).distinct('instructor'))
    hours={}
 

    correction_time=db.labs.aggregate([  {"$match": {'lab':lab_prefix}  },
            { "$group": {  "_id":"$instructor",   "correction_time": {   "$avg": "$correction_time"     }    }  } ])


    result={'-The number of opened PR is': opened_pr,
    '-The number of closed PR is': closed_pr,
    'The percentage of completeness is': percentage,
    'Number of missing PR is': missing_pr,
    'Distinct memes': memes,
    'Instructors mean grade time in hours': correction_time
    
    }
  
    return dumps(result)






@app.route("/memeranking")
def memeRanking():
    """
    #Purpose: This function returns the most ussed meme for datamad0820 for each lab
"""
    
    result=db.labs.aggregate([
        { "$group": {  "_id":{"lab":"$lab", "meme":"$meme2"}  ,
            "count": {
                "$sum": 1
            }
            }
        },
        {
            "$sort": {
            "_id.meme": 1,
            "count": 1
            }
        },
        {
            "$group": {
            "_id": {
                "category": "$_id.meme"
            },
            "name": {
                "$first": "$_id.lab"
            }
           
            }
        }
        ])

    return dumps(result)





@app.route("/lab/<lab_prefix>/meme")
def randomMeme(lab_prefix):
    """
    #Purpose: Get a random meme (extracted from the ones used for each student pull request) for that lab.
    #Params: The lab-prefix to be analyzed (its name). Example: lab-scavengers
    #Returns: a random meme
"""
    
    projection = {"_id":0, "meme1":1}
    result=db.labs.aggregate([  
        { "$match": { "$and": [{"lab": lab_prefix} ,{"pull_request_status": "closed"}]}}, 
        { "$sample": {"size": 1} }, 
        {"$project":projection}])

    return dumps(result)


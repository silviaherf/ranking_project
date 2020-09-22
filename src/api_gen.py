import os
from dotenv import load_dotenv
load_dotenv()
import requests
from flask import Flask
from flask import request, Response
#from src.helpers.json_response import asJsonResponse
import re
from src.database import db

app = Flask("ranking")

@app.route("/student/create/<studentname>")
def createStudent(student):
    studentname=student['name']
    db.students.insert(student)
    #res=requests.get(f'http://0.0.0.0:3000/student/create/{studentname}')
    

    projection = {"id": 1}
    searchRE = re.compile(f"{studentname}", re.IGNORECASE)
    foundStudent = db["github"].find_one(
        {"name": searchRE}, projection)

    if not foundStudent:
        # Set status code to 404 NOT FOUND
        return {
            "status": "not found",
            "message": f"No student found with name {foundStudent} in database"
        }, 404

  
    return foundStudent
        

"""

@app.route("/student/create/<studentname>")
#@asJsonResponse
def searchStudent(studentname):
    
    if not studentname:
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
        "searchQuery": studentname,
        "student": foundStudent
    }

"""

"""
@app.route("/student/create/prueba")
#@asJsonResponse
def searchStudent():
    
    return {
        "status": "OK",
        "message": 'esto es una prueba',

    }

"""


"""
@app.route("/student/all")
#@asJsonResponse
def allStudents():
    
    if not studentname:
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
        "searchQuery": studentname,
        "student": foundStudent
    }

"""






"""

@app.route("/lab/create")
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


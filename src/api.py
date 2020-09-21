import os
from dotenv import load_dotenv
load_dotenv()
import requests
from src.app import app
from flask import request, Response
#from src.helpers.json_response import asJsonResponse
import re
from src.database import db


def get_pr(i=0,api_key=os.getenv('GH_APIKEY'),i=1):
    
    """
    This function gets information out of an API for the year previously entered as a terminal argument.
    """
    baseUrl="https://api.github.com"
    endpoint=f'/repos/ironhack-datalabs/datamad0820/pulls?state=closed&page={i}'
    url = f"{baseUrl}{endpoint}"


    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    res = requests.get(url, params=query_params)
    #res = requests.get(url, params=query_params, headers=headers)
    print(f"Request data to {res.url} status_code:{res.status_code}")
    
     if res.status_code != 200:
        
        raise ValueError(f'Invalid Github API call: {data["message"]}\nSee more in {data["documentation_url"]}')
        
    else:
        print(f"Requested data to {baseUrl}; status_code:{res.status_code}")
        
        return res



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
        "company": foundStudent
    }

"""
import os
from dotenv import load_dotenv
load_dotenv()
import requests
from src.app import app
from flask import request, Response
#from src.helpers.json_response import asJsonResponse
import re
from src.database import db


def get_url(i=1,api_key=os.getenv('GH_APIKEY')):
    
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
def get_pr():
    """
        This function takes out every page of pull requests from the previuos get_url query"
    """
    response=get_url()

    print('Loading page 1')

    i=2
    while len(re.findall('last',response.headers['link']))==0:
        try:
            print(f'Loading page {i+1}')
            reviews=(get_url(i=i))
            i+=1
            
        except ValueError:
            break
"""

#Pendiente sacar los valores correctos
def get_student(res,i=0): 
    data=res.json()
    return student={
        'name':data[i]['title'],
        'lab': data[i]['title'],
        'pull_request':data[i]['title'],
        'meme':data[i]['title']

    }


 for i in len(data)
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
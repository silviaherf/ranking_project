import os
from dotenv import load_dotenv
load_dotenv()
import requests
#from flask import request, Response
#from src.helpers.json_response import asJsonResponse
import re
from src.database import db


def get_url(i=1,api_key=os.getenv('GH_APIKEY')):
    
    """
    This function gets information out of an API for the year previously entered as a terminal argument.
    """
    baseUrl="https://api.github.com"
    endpoint=f'/repos/ironhack-datalabs/datamad0820/pulls?state=all&page={i}'
    url = f"{baseUrl}{endpoint}"


    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    res = requests.get(url, headers=headers)
    #res = requests.get(url, params=query_params, headers=headers)
    print(f"Request data to {res.url} status_code:{res.status_code}")
    
    if res.status_code != 200:
        
        raise ValueError(f'Invalid Github API call: {data["message"]}\nSee more in {data["documentation_url"]}')
        
    else:
        print(f"Requested data to {baseUrl}; status_code:{res.status_code}")
        
        return res



def get_pages_students(i=1):
    """
        This function takes out every page of pull requests from the previuos get_url query
    """
    students=[]
    n_pages=int(re.search(r'\d{2}',re.search(r'\d{2}\>\;\srel="last"',get_url(i=1).headers['link']).group()).group())
    for page in range(i,n_pages):
        try:
            print(f'Loading page {page}')
            data=get_url(i=page).json()
            students.append([get_student(data,i=j) for j in range(0,len(data))])
            
        except ValueError:
            raise ValueError
    return students




#Pendiente sacar los valores correctos de meme,lab y times
def get_student(data,i=0): 
    lab=re.search(r'[lab-].*\]',data[i]['title']).group().split(']')[0]
    return {
        'name':data[i]['user']['login'],
        'join':'buscar @',
        'comentario':'buscar nombre',
        'lab': lab,
        'pull_request':data[i]['id'],
        'pull_request_status':data[i]['state'],
        'instructor': data[i]['assignees'][0]['login'] ,
        'pull_request_close_time': data[i]['closed_at'],
        'last_commit_time': data[i]['updated_at'],
        'meme':data[i]['title']

    }

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
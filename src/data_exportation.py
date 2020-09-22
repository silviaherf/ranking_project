import os
from dotenv import load_dotenv
load_dotenv()
import requests
import re
from bs4 import BeautifulSoup
import json




def get_pull_requests(api_key=os.getenv('GH_APIKEY'),i=1):
    
    """
    This function gets information of all pull requests in datamad0820 repo. In case it is specified, the number of the resulting page can be changed
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
    
    data = res.json()
    if res.status_code != 200:
        
        raise ValueError(f'Invalid Github API call: {data["message"]}\nSee more in {data["documentation_url"]}')
        
    else:
        print(f"Requested data to {baseUrl}; status_code:{res.status_code}")
        
        return res

def get_url(url,api_key=os.getenv('GH_APIKEY')):
    
    """
    This function makes a request to a URL and returns its response.
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    res = requests.get(url, headers=headers)
    #res = requests.get(url, params=query_params, headers=headers)
        
    data = res.json()
    if res.status_code != 200:
        
        raise ValueError(f'Invalid Github API call: {data["message"]}\nSee more in {data["documentation_url"]}')
        
    else:
        print(f"Requested data to {url}; status_code:{res.status_code}")
        
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





def get_student(data,i=0): 
    """
    This function takes out the information needed in MongoDB. 
    The parameter needed is data, the selected response as json format.

    """

    lab=re.search(r'[lab-].*\]',data[i]['title']).group().split(']')[0]
           
    if data[i]['state']=='closed':
        pull_request_closed_day=re.search(r'\d{4}\-\d{2}\-\d{2}',data[i]['closed_at']).group()
        pull_request_closed_time=re.search(r'\d{2}\:\d{2}\:\d{2}',data[i]['closed_at']).group()
    else:
        pull_request_closed_day=''
        pull_request_closed_time=''


    pull_request_created_day=re.search(r'\d{4}\-\d{2}\-\d{2}',data[i]['created_at']).group()
    pull_request_created_time=re.search(r'\d{2}\:\d{2}\:\d{2}',data[i]['created_at']).group()
    
    if data[i]['assignees']:
        instructor=data[i]['assignees'][0]['login']
    else:
        instructor=''
    
    dic={
        'name':data[i]['user']['login'],
        'lab': lab,
        'pull_request':data[i]['id'],
        'pull_request_status':data[i]['state'],
        'instructor': instructor ,
        'pull_request_closed_day': pull_request_closed_day,
        'pull_request_closed_time': pull_request_closed_time,
        'pull_request_created_day': pull_request_created_day,
        'pull_request_created_time': pull_request_created_time,
    }

    if data[i]['state']=='closed':    
        comment=get_url(data[i]['comments_url']).json()
        memes={}
        if len(comment)>0:
            for n,encuentra in enumerate(re.findall(r'http.*\)',comment[0]['body'])):
                meme=encuentra.split(')')
                memes.update({f'meme{n+1}':meme[0]})
            
        else:
            memes.update({f'meme':''})
        dic.update(memes)

    

    if data[i]['body']:
        mentions={}
        mention_encuentra=re.findall(r'\@\w+',data[i]['body'])
        for n,mention in enumerate(mention_encuentra):
            mentions.update({f'mentioned{n+1}':mention})
        dic.update(mentions)
    
    if type(requests.get(data[i]['issue_url']).json())==list:
        joins={}
        for n,join in enumerate(requests.get(data[i]['issue_url']).json()):
            if re.search(r'join',join['body']):
                joins.update({f'join{n+1}':join['user']['login']})
            dic.update(joins)
    

    return dic

def export_json(students):
    with open('students.json', 'w') as json_file:
        json.dump(students, json_file)
    return 'JSON file exported'





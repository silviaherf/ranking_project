import os
from dotenv import load_dotenv
import requests

def get_repos(endpoint='/repos/ironhack-datalabs/datamad0820/pulls',api_key=os.getenv('GH_APIKEY'),query_params={}):
    """
    This function gets information out of an API for the year previously entered as a terminal argument.
    """
    baseUrl="https://api.github.com"
    url = f"{baseUrl}{endpoint}"


    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    # make the request and get the response using HTTP GET verb 
    res = requests.get(url, params=query_params, headers=headers)
    print(f"Request data to {res.url} status_code:{res.status_code}")
    
    data = res.json()


    if res.status_code != 200:
        data=res.json()
        raise ValueError(f'Invalid Github API call: {data["message"]}\nSee more in {data["documentation_url"]}')
        
    else:
        print(f"Requested data to {baseUrl}; status_code:{res.status_code}")
        data=res.json()
        return data



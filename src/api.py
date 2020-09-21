import os
from dotenv import load_dotenv
import requests

def get_pr(i=0,api_key=os.getenv('GH_APIKEY'),i=0):
    
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





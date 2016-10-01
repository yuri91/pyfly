import requests
import json
import time
from pathlib import Path

with (Path(__file__).parent/"apikey.txt").open() as f:
    api_key = f.read().strip()

params = {
    'originplace':"AMS",
    'destinationplace':"GOA",
    'outbounddate':"2016-10-13",
    'inbounddate':"2016-10-16",

    'adults':1,
    'country':"it",
    'currency':"eur",
    'locale':"it-IT",
    'locationschema': "Sky",

    'apiKey':api_key
}

json_header = {"Accept":"application/json"}
form_header = {"Content-Type":"application/x-www-form-urlencoded"}

newsession_headers={**json_header,**form_header}
newsession_url = "http://partners.api.skyscanner.net/apiservices/pricing/v1.0"


def newsession(api_key):
    resp = requests.post(newsession_url,
                         data=params,
                         headers=newsession_headers)
    location = resp.headers.get('Location',None)
    return resp.status_code, location

def poll(location, api_key):
    resp = requests.get(location,
                        params={'apiKey':api_key},
                        headers=json_header)
    return location, resp.status_code, resp.json()

if __name__ == "__main__":

    code, location = newsession(api_key)
    print(code)
    time.sleep(2)
    location, code, data = poll(location,api_key)
    print(code)
    print(data)


import urllib.request
from urllib import request
import json

count = 0
limit = 100

secret = open('token.txt', 'r')
token = secret.read()
secret.close()
# loading in the token without uploading it to GitHub

response = 0
response_offset = 0  # sets the record the api call will begin with

api_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locations&limit=39&offset=' + str(response_offset)


while response < 39:
    output = request.Request(api_url, headers={'token': token})
    with request.urlopen(output) as out:
        json_obj = json.load(out)
    with open(f'responses/locations_{count}.json', 'w') as file:
        json.dump(json_obj, file)

        count += 1
        response_offset += limit

'''
Created on 30-Nov-2025

@author: vishw
'''
import requests

request_body={"name": "MOTOROLA G52",
   "data": {
      "year": 2021,
      "price": 14000,
      "CPU model": "Snapdragon",
      "Hard disk size": "128 GB"}
   }

response =requests.post("https://api.restful-api.dev/objects",json=request_body)  
print(response)
print(response.status_code)

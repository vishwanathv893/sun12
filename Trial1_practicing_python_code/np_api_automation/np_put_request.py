'''
Created on 30-Nov-2025

@author: vishw
'''
import requests

response_body ={
   "name": "MOTO g52 ",
    "shape":"bar",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
     
   }
   
}

response =requests.put("https://api.restful-api.dev/objects/ff8081819782e69e019ad7a3de0a4801",json= response_body)
print("response:",response)
status_code = response.status_code
print("response.status_code:",status_code)
response_body = response.json()
print("response.json():",response_body)
object_id = response_body["id"]
print("object_id:", object_id)







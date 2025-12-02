'''
Created on 30-Nov-2025

@author: vishw
'''
import requests

response=requests.get("https://api.restful-api.dev/objects/7")
print("response:",response)
print("response.status_code :",response.status_code)
response_body =response.json()
print(response_body)
object_id=response_body["id"]
print("object_id:",object_id)
data=response_body["data"]
price=(data["price"])
print(price)




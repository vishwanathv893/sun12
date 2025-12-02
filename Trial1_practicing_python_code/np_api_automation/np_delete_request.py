'''
Created on 30-Nov-2025

@author: vishw
'''
import requests

response =requests.delete("https://api.restful-api.dev/objects/ff8081819782e69e019ad54c81c7448c")
print(response.status_code)

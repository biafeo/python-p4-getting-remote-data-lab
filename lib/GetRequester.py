import requests
import json

class GetRequester:

    def __init__(self, url, name=None, occupation=None):
        self.url = url
        self.name = name
        self.occupation = occupation 
        
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        response = requests.get(self.url)
        return response.json()
    
url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
name = 'John'
occupation = 'Engineer'

requester = GetRequester(url, name, occupation)
results = requester.get_response_body()
print(results)

results_json = requester.load_json()
print(json.dumps(results_json, indent=1))
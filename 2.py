#Create an organization repository
import requests
import json
base_url="https://api.github.com/"
authToken="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"
todo={"name":"abc","description":"This is your third repository","private":False,"has_issues":True,"has_projects":True,"has_wiki":True}
url=base_url + "orgs/repoassignment1/repos"
print(url)
token = {
        'Access': authToken,
        'Content-Type': 'application/json'
}
response=requests.post(url,data=json.dumps(todo),auth=(authToken,''))
print(response)
print(response.json())
#201
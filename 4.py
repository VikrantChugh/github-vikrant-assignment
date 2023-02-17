#{"name":"Hello-World","description":"This is your first repository","homepage":"https://github.com","private":true,"has_issues":true,"has_projects":true,"has_wiki":true}
#Update a repository
import requests
import json
base_url="https://api.github.com/"
authToken="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"
todo={"name":"project","description":"This is your third repository","private":False,"has_issues":True,"has_projects":True,"has_wiki":True}
url=base_url + "repos/VikrantChugh/hii"
print(url)
response=requests.patch(url,data=json.dumps(todo),auth=(authToken,''))
print(response)
print(response.json())
#    PATCH
# /repos/{owner}/{repo}
#200
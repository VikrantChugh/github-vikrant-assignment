#Enable automated security fixes
import requests
import json
base_url="https://api.github.com/"
authToken="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"
todo={'Accept': "application/vnd.github+json" ,
"Authorization": 'Bearer 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',
   "X-GitHub-Api-Version": "2022-11-28"} 
url=base_url + "repos/VikrantChugh/fedproject/automated-security-fixes"
print(url)
response=requests.put(url,data=json.dumps(todo),auth=(authToken,''))
print(response)
print(response.json())
#    /repos/{owner}/{repo}/automated-security-fixes
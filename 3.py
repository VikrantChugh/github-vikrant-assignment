#Get a repository
import requests
base_url="https://api.github.com/"
token="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"
def getuser():
    url=base_url + "repos/VikrantChugh/fedprojects"
    print(url)
    response=requests.get(url,auth=(token, ''))
    
    print(response)
    print(response.json())
getuser()    
#200
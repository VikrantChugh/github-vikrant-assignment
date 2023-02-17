#delete repo
import requests
import json
base_url="https://api.github.com/"
authToken="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"
url=base_url + "repos/VikrantChugh/fedproject"
print(url)
response=requests.delete(url,auth=(authToken,''))
print(response)
print(response.json())
#204
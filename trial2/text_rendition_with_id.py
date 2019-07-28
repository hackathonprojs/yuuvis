import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'



headerDict['Ocp-Apim-Subscription-Key'] = '65130be7439d404ab00348dc32a4341a'




session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/441061bf-bb5a-48a7-8a82-c74de40f1bb6/contents/renditions/text'), headers=headerDict)
print(response)

print(response.content)
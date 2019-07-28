import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'


headerDict['Content-Type'] = 'application/json'






headerDict['Ocp-Apim-Subscription-Key'] = '65130be7439d404ab00348dc32a4341a'




session = requests.Session()


#relative path to your new query file
queryFilePath = './query.json'
response = session.post(str(baseUrl+'/dms/objects/search'), data=open(queryFilePath, 'rb'), headers=headerDict)
print(response.json())

import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

#update this and two paths below
myFileName = 'test_pdf.pdf'




headerDict['Ocp-Apim-Subscription-Key'] = '65130be7439d404ab00348dc32a4341a'




session = requests.Session()


#relative path to your content file
contentFilePath = './test_pdf.pdf'
#relative path to your metadata file
metaDataFilePath = './metadata.json'

multipart_form_data = {
    'data' :('data.json', open(metaDataFilePath, 'rb'), 'application/json'),
    'cid_63apple' : (myFileName, open(contentFilePath, 'rb'), 'application/pdf')
}

response = session.post(str(baseUrl+'/dms/objects'), files=multipart_form_data, headers=headerDict)
print(response.json())


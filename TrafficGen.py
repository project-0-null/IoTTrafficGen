import requests
import json
import pprint

url = 'http://172.16.30.113:9090/ngsi-ld/v1/entities'
headers = {'content-type': 'application/json'}
payload = {'type': 'https://uri.fiware.org/ns/dataModels#Building'}

def getRequest(url: str, payload: dict, headers: dict):
    r = requests.get(url, params=payload, headers=headers)

    print("Request URL: " + r.url)
    print()
    pprint.pprint(r.json())

    return r

r = getRequest(url, payload, headers)


"""
url = 'http://localhost:5000'
headers = {'content-type': 'application/json'}
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post(url, headers=headers, data=json.dumps(payload))
r.encoding = 'utf-8'

print("Request URL: " + r.url)
print("Response: " + r.json)
"""




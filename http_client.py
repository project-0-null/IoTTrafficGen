import requests

def create_entitie(url, data, params):
    try:
        headers = {'content-type': 'application/ld+json'}
        response = requests.post(url, json=data, headers=headers, params=params)
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, str(e)

def update_attr_value(url, data, entity_id, attr_name, entity_type):
    try:
        url = f"{url}/urn:ngsi-ld:{entity_type}:{entity_id}/attrs/{attr_name}"
        headers = {
            'Content-Type': 'application/json',
            'Link': '<https://fiware.github.io/data-models/context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
            'Accept': 'application/json'
        }
        response = requests.patch(url, json=data, headers=headers)
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, str(e)
    
def get_entity(url, params):
    try:
        url = f"{url}"
        headers = {'Accept': 'application/ld+json'}
        response = requests.get(url, params=params, headers=headers)
        return [response.status_code, response.text]
    except requests.exceptions.RequestException as e:
        return None, str(e)
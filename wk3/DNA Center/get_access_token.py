import requests
def get_access_token():
    url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
    username = "devnetuser"
    password = "Cisco123!"

    response = requests.post(url, auth=(username, password), verify=False)
    if response.ok:
        token = response.json()['Token']
        return token
    else:
        response.raise_for_status()
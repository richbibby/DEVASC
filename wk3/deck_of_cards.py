import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
print(json.dumps(response.json(), indent=2))
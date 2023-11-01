import requests
import json

url = "http://localhost:5000/api/chat"
headers = {'Content-Type': 'application/json'}
data = {"message": "javascriptについて簡単に教えてください。"}

response = requests.post(url, headers=headers, data=json.dumps(data))
res_data = response.json()

print(res_data)

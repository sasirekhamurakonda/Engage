import requests
import json
url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-tknvs/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "Event",
    "database": "Engage",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'loibXia7tC0LAKsoDLckPrAWOgabYz7fmNZtZFwQOMCvn3jTcoGGD8zqAIbm9FKC', 
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
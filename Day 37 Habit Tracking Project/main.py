import requests
from datetime import datetime

USERNAME = "bigzy"
TOKEN = "tokenhere123"
pixela_endpoint = 'https://pixe.la/v1/users'

# Create Account
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

# Create Graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': "graph1",
    'name': "Cycling Graph",
    'unit': "Km", 
    'type': "float",
    'color': "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Post Value to graph

graphPost_endpoint = f"{graph_endpoint}/{graph_params['id']}"

today = datetime.now().strftime("%Y%m%d")
post_params = {
    "date": today,
    "quantity": "5",
}

# Post
# esponse = requests.post(url=graphPost_endpoint, headers=headers, json=post_params)
# rint(response.text)


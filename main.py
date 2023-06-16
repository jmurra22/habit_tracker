import requests
from datetime import datetime
import os

USERNAME = "jmurra225"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Coding Graph",
#     "unit": "Minutes",
#     "type": "float",
#     "color": "ajisai",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? ")
}

pixel_data = requests.post(url=pixel_creation, json=post_params, headers=headers)
print(pixel_data.text)

# new_pixel_data = {
#     "quantity": "75"
# }
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# delete_pixel = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_pixel.text)

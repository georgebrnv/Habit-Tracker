import requests
from datetime import datetime
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("API_TOKEN")
GRAPH_ID = "codinggraph1"

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now().strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_params = {
    "date": input("When did you code? (YYYYMMDD)"),
    "quantity": input("How many hours did you code?"),
}

pixel_updt_params = {
    "quantity": input("How many hours did you code?"),
}

graph_updt_params = {
    "unit": "Hour(s)",
    "color": "shibafu",
}

# _______________________________________________________________________________________
# UNCOMMENT A LINE OF CODE TO COMPLETE A REQUEST


# Create an account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Update graph
# response = requests.put(url=pixel_endpoint, json=graph_updt_params, headers=headers)
# print(response.text)

# Delete a graph
# response = requests.delete(url=pixel_endpoint, headers=headers)
# print(response.text)

# Post a pixel
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# Update a pixel
# response = requests.put(url=f"{pixel_endpoint}/20231026", json=pixel_updt_params, headers=headers)
# print(response.text)

# Delete a pixel
# response = requests.delete(url=f"{pixel_endpoint}/20231026", headers=headers)
# print(response.text)

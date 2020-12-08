import requests
from datetime import datetime

USERNAME = "devtest234"
TOKEN = "asdfwer234234fsd"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now().strftime("%Y%m%d")

post_pixel_config = {
    "date": today,
    "quantity": "3",
}

# Create Pixel
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}"

put_pixel_config = {
    "quantity": "10",
}

# Update Pixel
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(response.text)

# Delte Pixel
# response = requests.delete(url=put_pixel_endpoint, headers=headers)
# print(response.text)

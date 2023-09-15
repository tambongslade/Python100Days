import requests
pixela_endpoint= "https://pixe.la/v1/users"
TOKEN = "sdfg21fsfd12daze123sf"
USERNAME = "tambong2023",
user_params = {
    "token": TOKEN,
    "userName": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes",
}
graph_config = {
    "id": "graph1",
    "name": "No touching",
    "unit": "Days",
    "type": "int",
    "color": "ajisai"

}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER_TOKEN" : TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
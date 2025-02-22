import requests

api_params = {
    "amount":10,
    "type":"boolean",
    "category":18
}


response = requests.get(url= "https://opentdb.com/api.php",params=api_params)
response.raise_for_status()
data = response.json()


question_data = data["results"]
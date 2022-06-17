import requests

api_url = "https://www.uniprot.org/uniprotkb/P12345"
response = requests.get(api_url)
print(response.status_code)
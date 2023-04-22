import requests
url="http://localhost:5000/"
response=requests.get(url)
output=response.text
assert output == 'Hello world!'
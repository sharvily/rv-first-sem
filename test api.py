import requests 
test_id = "id"
test_name = "Google Pixel 6 Pro"

url = f"https://api.restful-api.dev/objects/{id}"
response = requests.get(url)
data = response.json()
xyz = data[test_name]
print(xyz)




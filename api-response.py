import requests

# Download a web page
response = requests.get("https://google.com")
print(response.status_code)  # Should print 200
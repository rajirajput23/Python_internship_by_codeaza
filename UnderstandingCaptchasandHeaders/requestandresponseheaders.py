import requests
from bs4 import BeautifulSoup

#URL to request
url="https://www.example.com/"

#GET Request to the url
resp =requests.get(url)
print(resp) 

# Printing the request headers
print("Request Headers:")
for header, value in resp.request.headers.items():
    print(f"{header}: {value}")


# Printing the response headers
print("\nResponse Headers:")
for header, value in resp.headers.items():
    print(f"{header}: {value}")
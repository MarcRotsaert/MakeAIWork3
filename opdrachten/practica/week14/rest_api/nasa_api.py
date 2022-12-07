import requests

reqUrl = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY"

headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
}

payload = ""

response = requests.request("GET", reqUrl, data=payload, headers=headersList)

print(response.text)
print(type(response))

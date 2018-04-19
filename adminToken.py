import requests

url = "https://malmu06-s10712.ca.com:8443/ca/api/sso/services/login/v1/token"

headers = {
    'authorization': "Basic c2l0ZW1pbmRlcjpzaXRlbWluZGVy",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, headers=headers, verify=False)

print(response.text)

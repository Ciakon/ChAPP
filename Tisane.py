import requests

url = "https://api.apilayer.com/tisane/parse"

payload = {"language": "en", "content":"Fuck you, you piece of shit.", "settings": {"abuse" : True}}
headers= {
  "apikey": "bZAnoqOOiKPxCSuohjteJ4DOnFGar07s",
  'content-type':'application/json'
}

response = requests.request("POST", url, headers=headers, json = payload)

status_code = response.status_code
result = response.text

print(status_code)
print(result)

#def checkProfanity(message):
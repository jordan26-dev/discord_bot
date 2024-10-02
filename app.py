import requests

# automate discord messages
# open discord channel > inspect > send test message > goto Network tab > find messages > Look in Headers and Payload tab

url = "discord url"


payload= {
    "content" : "Hello world! Test"
}

headers = {
    "Authorization" : "your auth token"
}

res = requests.post(url, payload, headers=headers)    

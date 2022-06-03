import requests

# Making a POST request
r = requests.post('https://httpbin.org / post', data ={'key':'value'})

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.json())

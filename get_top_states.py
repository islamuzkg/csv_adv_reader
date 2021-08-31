import requests

r = requests.get('https://corona.lmao.ninja/v3/covid-19/states')
data = r.content
print(r)
print(data)
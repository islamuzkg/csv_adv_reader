import json
# from urllib.request import urlopen

# with urlopen("https://corona.lmao.ninja/v3/covid-19/states?format=json") as response:
#   source = response.read()
# data = json.loads(source)
# print("----------------------------------------------------------")


from urllib.request import Request, urlopen
def read_jdata():
   req = Request('https://corona.lmao.ninja/v3/covid-19/states?format=json', headers={'User-Agent': 'Mozilla/5.0'} )
   webpage = urlopen(req).read()
   data = json.loads(webpage)
   return(json.dumps(data, indent=2))

print("==========================================")
D = read_jdata()
print(D)
import requests
import time
import json
# find top 5 state.
r = requests.get('https://corona.lmao.ninja/v3/covid-19/states?format=json')
data = r.json()
# jdata = json.dumps(data, indent=2)
# str_data_state = json.dumps(data[0]['state'])
# str_data_cases = json.dumps(data[0]['cases'])
# data_sc = f'{str_data_state} {str_data_cases}'
# print("----------------------------------------------------------")
# print(data_sc)
# print(len(data))

# Dictionary list creation 
t1 = time.perf_counter()
results = []
for key in data:
  str_data_state = key['state']
  str_data_cases = key['cases']
  data_sc = f'{str_data_state} {str_data_cases}'
  d_data = {
    'state': str_data_state,
    'cases': str_data_cases
  }
  results.append(d_data)
  #time.sleep(3)
  time.sleep(r.elapsed.total_seconds())
  # below break is used to print only 1st line of a list
  #break
t2 = time.perf_counter()
#print(results)
print(f'finished in  {t2-t1} seconds')
  #print(data_sc)
with open('state_cases.json', 'w') as f:
  json.dump(results, f, indent=2)
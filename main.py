import json

def sort_cases(case):
  return case['cases']


with open('state_cases.json', 'r') as f:
  data = json.load(f)
  #print(data)

print('==========================')
data.sort(key=sort_cases, reverse=True)
data_str = json.dumps(data, indent=2)
#print(data[0]['state'])

for key in range(0, 5):
  state = data[key]['state']
  cases = data[key]['cases']
  sc = f'{state} {cases}'
  print(sc)


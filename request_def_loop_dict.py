import requests
import json
# find top 5 state.
r = requests.get('https://corona.lmao.ninja/v3/covid-19/states')
data = r.json()
# print(data[0].values())
# print(len(data))
#print(data)
print("----------------------------------------------------------")

Dic = []
for key in range(0, len(data)-1):
  states = data[key]["state"]
  cases = data[key]["cases"]
  sc = {states: cases}
  Dic.append(sc)
print(Dic)

# Write a data into a file in a json format
# with open('new_states.json', 'w') as f:
#   json.dump(Dic, f, indent=2) 

# with open('new_states.json') as f:
#   j_data = json.load(f)
#   print(type(j_data))


# Creat double loop



#
# His questions: How efficient is your code? (2*n) are you familiar with notation O ?
#
# You will be supplied with two data files in CSV format . The first file contains statistics about various dinosaurs. The second file contains additional data. Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) Where g = 9.8 m/s^2 (gravitational constant) Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
#
# import csv
# import math
#
# def calculator(STRIDE_LENGTH, LEG_LENGTH):
#   g = 9.8
#   speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
#   return speed
#
# def OrderBipadalDInosaurs(file_path_1,file_path_2):
#   bipedals = []
#   dic2={}
#   with open(file_path_2) as data2:
#     file2=csv.DictReader(data2)
#     for key in file2:
#       #if key == "bipedal":
#       if key["STANCE"] == "bipedal":
#         bipedals.append(key["NAME"])
#         print(bipedals)
#         dic2[key["NAME"]]=key["STRIDE_LENGTH"]
#  
#   dic1={}
#   with open(file_path_1) as data1:
#     file1=csv.DictReader(data1)
#     for key in file1:
#       for i in bipedals:
#         if i in key["NAME"]:
#           dic1[key["NAME"]]=key["LEG_LENGTH"]
#
#   finaldic={}
#   for key, value in dic1.items():
#       if key in dic2.keys():
#           STRIDE_LENGTH=float(dic2[key])
#           LEG_LENGTH=float(value)
#           speed=calculator(STRIDE_LENGTH, LEG_LENGTH)
#           finaldic[key]=speed
#
#   finalsorted=sorted(finaldic.items(), key=lambda x: x[1], reverse=True)
#   print(finalsorted)
#   #for key, value in finalsorted:
#   #    print(key)
#
# OrderBipadalDInosaurs("dataset1.csv","dataset2.csv")
#
#
# def isPoliandrome(arg): 
#   value=str(arg) 
#   if value == value[::-1]: 
#       print("YES it is polindrome") 
#   else: 
#       print("NO its NOT") 
#
#
# A=[5,2,0,3,0,1,6,0,5,0] 
#
# print(sorted(A)) 
# def sortArray(arr): 
#   result=sorted(arr) 
#   for i in result: 
#       if 0 in result: 
#           result.append(result.pop(result.index(0))) 
#   return result 
# print(sortArray(A))

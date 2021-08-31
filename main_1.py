# import csv

# with open('./dataset1.csv') as infile:
#     reader = csv.reader(infile, delimiter=',')
#     title = next(reader)
#     found_section = False
#     header = None
#     LG_index = None
#     LG_sum = 0.0
#     for row in reader:
#         if not found_section:
#             if len(row) > 0:
#                 if row[0] == "name":
#                     header = next(reader)
#                     LG_index = header.index("LG")
#                     found_section = True
#         else:
#             if len(row) > 0:
#                 print(float(row[LG_index]))
#                 LG_sum += float(row[LG_index])
#             else:
#                 break
#     print(LG_sum)

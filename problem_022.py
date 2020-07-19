# Date: 2020.07.18
# Answer: 

import string
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)


names = []
# input data from file into array
with open('data/data_022.txt') as data:
    for cnt, line in enumerate(data):
        # print("Line {}: {}".format(cnt, line))
        names=line.split(",")

names.sort()
print(alphabet_list)
name_score = []




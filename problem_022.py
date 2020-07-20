# Date: 2020.07.19
# Answer: 871198282

import string
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

def input_names(path):
    list_from_file = []
    # input data from file into array
    with open(path) as data:
        for cnt, line in enumerate(data):
            list_from_file=line.split(",")
    return list_from_file

def get_letter_score(letter):
    return alphabet_list.index(letter)+1

def get_name_value(name):
    name_value = 0
    for i in name:
        name_value += get_letter_score(i)
        #print(letter_score,name_value,position)# alphabet_list.index(i))
    return name_value

def get_name_score(name,position):
    return get_name_value(name)*position

def get_total_score(list_of_names):
    sum = 0
    for cnt,name in enumerate(list_of_names):
        #print(cnt,name)
        sum += get_name_score(name.strip('"'),cnt+1)
    return sum

#print(get_total_score(names))
#print(get_total_score("COLIN"))

#print(len(names))
# print(get_letter_score('Z'))
# print(get_name_value("COLIN"))
# print(get_name_score("COLIN",938))
#print(names.index('"COLIN"'))

names = []
names = input_names('data/data_022.txt')
names.sort()
print(get_total_score(names))
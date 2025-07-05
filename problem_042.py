# Date: 2025.07.05
# Answer: 162

import math
import string

def check_triangle(num):
    val = num*2
    low = math.floor(math.sqrt(val))

    if((0.5*low*(low+1))==num):
        # print(num,low,low+1,(0.5*low*(low+1)))
        return True
    return False

def word_value(word):
    letter_to_number = {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}
    letters = list(word.lower())
    value=0
    for item in letters:
        value+=letter_to_number.get(item)

    return value

def process_file(file):
    with open(file) as data:
        for cnt, line in enumerate(data):
            list_from_file=line.split(",")
    
    num_triangles = 0
    for word in list_from_file:
        x = word.replace('"','').lower()
        value = word_value(x)
        if check_triangle(value):
            # print(x,value)
            num_triangles+=1
    print(len(list_from_file))
    return num_triangles


if __name__ == "__main__":
    print(process_file("data/0042_words.txt"))

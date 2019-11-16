import math

def make_list(value):
    list = []
    for i in range(len(str(value))):
        list.append(str(value)[i])
    return list

def is_palindrome(value):
    list = make_list(value)
    for i in range(math.ceil(len(list)/2)):
        if list[i] != list[len(list)-1-i]:
            return False
    return True

largest = 0
for i in range(100,999):
    for j in range(100,999):
        if is_palindrome(i*j) and i*j>largest:
            largest = i*j

print("largest: ",largest)


#print(is_palindrome(12354321))





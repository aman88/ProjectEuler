# Date: 2025.07.22
# Answer: 7652413

import math
from itertools import permutations

def get_perms(value):
    val_list = list(str(value))
    perms = permutations(val_list)
    val_list = []
    for item in perms:
        val_list.append(int("".join(item)))
    return val_list

def is_prime(value):
    for i in range(2,math.ceil(math.sqrt(value)+1)):
        if value % i == 0:
            return False
    return True

def is_pandigital(str_value):
    len_val = len(list(str_value))
    set_val = set(list(str_value))

    for i in range(1,len_val+1):
        if str(i) not in set_val:
            return False
    return True

digits = []
prime = 0
for i in range(1,10):
    digits.append(str(i))
    num = int(''.join(digits))
    print(num)
    perms = get_perms(num)
    for item in perms:
        if is_prime(item):
            if item > prime:
                prime = item
                print(f"current val: {prime}")


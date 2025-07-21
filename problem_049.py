# Date: 2025.07.21
# Answer: 

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

def count_primes(list_vals):
    count = 0
    primes = []
    for item in list_vals:
        if is_prime(item):
            count += 1
            primes.append(item)
    return primes


for i in range(1000,10000):
    perms = get_perms(i)
    primes = count_primes(perms)
    result = []
    if len(primes) == 3:
        print(primes)
        primes = primes.sort()
        print(primes)
        if primes[0] - primes[1] == primes[1] - primes[2]:
            result.append([primes])
            print(result)




get_perms(1234)
# Date: 2025.07.20
# Answer: 

import math
from itertools import permutations
import time


def is_prime(value):
    for i in range(2,math.ceil(value/2+1)):
        if value % i == 0:
            return False
    return True

def rearranged_nums(value):
    list_permutations = []
    chars = list(str(value))
    for i in range(1,len(chars)+1):
        list_permutations.append(int("".join(chars[-i:]+chars[0:len(chars)-i])))
    return list_permutations

def is_circleprime(list):
    for item in list:
        if(not is_prime(item)):
            return False
    return True


if __name__ == "__main__":
    start_time = time.perf_counter()

    circleprime_set = set({2})
    for i in range(2,1000000):
        if(i%2==0):
            continue
        list_nums = rearranged_nums(i)
        if(is_circleprime(list_nums)):
            for item in list_nums:
                circleprime_set.add(item)
            # print(i)
        print(i, end='\r')

    print(f"Number of circle primes: {len(circleprime_set)}")
    print(circleprime_set)
    
    cur_time = time.perf_counter()
    elapsed_time = cur_time - start_time
    print(f"Function execution time: {elapsed_time:.6f} seconds")
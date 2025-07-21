# Date: 2025.07.20
# Answer: 

import math
from itertools import permutations
import time


def is_prime(value):
    if(value==1):
        return False
    for i in range(2,math.ceil(value/2+1)):
        if value % i == 0:
            return False
    return True

def truncatable(value):
    str_val = str(value)
    if not is_prime(value):
        return False
    for i in range(1,len(str_val)):
        if not is_prime(int(str_val[i:])):
            return False
        if not is_prime(int(str_val[:-i])):
            return False
    return True

if __name__ == "__main__":
    start_time = time.perf_counter()

    primes = []
    num = 11
    while len(primes) < 11:
        print(f"processing {num}",end="\r")
        if truncatable(num):
            primes.append(num)
            print(f"\n{num}")
        num += 2
        
    print(sum(primes))

    cur_time = time.perf_counter()
    elapsed_time = cur_time - start_time
    print(f"Function execution time: {elapsed_time:.6f} seconds")

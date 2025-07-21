# Date: 2025.07.20
# Answer: 872187

import math
from itertools import permutations
import time


def binary(value):
    bin_val = []
    while value > 0:
        remainder = value % 2
        value = value // 2
        bin_val.insert(0,str(remainder))
    return int("".join(bin_val))

def is_palindrome(value):
    for i in range(0,len(str(value))):
        # print(str(value)[i],str(value)[len(str(value))-1-i])
        if str(value)[i] != str(value)[len(str(value))-1-i]:
            return False
    return True




if __name__ == "__main__":
    start_time = time.perf_counter()

    palindromes = []
    for i in range(1,1000000):
        if is_palindrome(i) and is_palindrome(binary(i)):
            palindromes.append(i)
            print(i)

    sum = 0
    for item in palindromes:
        sum += item
    
    print(f"total is {sum}")
    
    cur_time = time.perf_counter()
    elapsed_time = cur_time - start_time
    print(f"Function execution time: {elapsed_time:.6f} seconds")

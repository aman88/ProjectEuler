# Date: 2025.07.20
# Answer: 40730

import math
from itertools import permutations
import time


def get_digits(value):
    list_digits = list(str(value))
    return list_digits

def get_sum(list):
    sum = 0
    for item in list:
        sum += math.factorial(int(item))
    return sum

if __name__ == "__main__":
    start_time = time.perf_counter()

    count = 0
    value = 3
    while value < 10000000000:
        print(f"value: {value} sum: {sum} count: {count}                       ", end='\r')
        list_digits = get_digits(value)
        sum = get_sum(list_digits)
        if(value == sum):
            count+=1
            print(f"value: {value} sum: {sum} count: {count}")
        if(sum > value):
            value = int(round(value+5.1,-1))
            continue
        value += 1
    
    cur_time = time.perf_counter()
    elapsed_time = cur_time - start_time
    print(f"Function execution time: {elapsed_time:.6f} seconds")
        

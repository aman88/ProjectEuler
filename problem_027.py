# Date: 2025.07..20
# Answer: -59231

import math

def is_prime(value):
    if value < 0:
        return False
    for i in range(2,math.ceil(value/2+1)):
        if value % i == 0:
            return False
    return True

def consecutive_primes(a,b):
    count = 0
    n=0
    while True:
        value = n*n+a*n+b
        if(is_prime(value)):
            count+=1
            n+=1
        else:
            return count

largest = 0
best_a = 0
best_b = 0
for a in range(-999,1000):
    for b in range (-1000,1001):
        print(f"currently processing {a} {b}                ",end="\r")
        count = consecutive_primes(a,b)
        if count>largest:
            largest = count
            best_a = a
            best_b = b
            print(f"a: {a} b: {b} longest sequence: {largest}")

# print(consecutive_primes(-9999,-1000))
# Date: 2025.07..20
# Answer: 443839

import math

def raise_power(value):
    return math.pow(value,5)

def get_digits(value):
    return list(str(value))

digits_fifth = []
for i in range(2,1000000):
    digits = get_digits(i)
    
    sum = 0
    for item in digits:
        sum += raise_power(int(item))
    if sum == i:
        digits_fifth.append(i)
        print(i)
    
total = 0
for item in digits_fifth:
    total += item
print(total)
# Date: 2025.07..20
# Answer: 45228

import math

def is_pandigital(str_value):
    len_val = len(list(str_value))
    set_val = set(list(str_value))

    for i in range(1,len_val+1):
        if str(i) not in set_val:
            return False
    return True

products = []
for i in range(0,10000):
    for j in range (0,100):
        print(f"processing: {i} {j}      ",end="\r")
        k = i*j
        str_val = "".join(str(i)+str(j)+str(k))
        if is_pandigital(str_val):
            if len(str_val) == 9:
                print(i,j,k)
                products.append(k)

prod = set(products)
print(products)
print(prod)
total = 0
for item in prod:
    total += item
print(f"total product sum: {total}")







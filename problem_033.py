# Date: 2025.07.21
# Answer: 100

import math

def cancel_values(i,j):
    i = list(str(i))
    j = list(str(j))
    if(i[0] == j[0]):
        i = i[1]
        j = j[1]
        # print(i,j)
        return int(i), int(j)
    if(i[0] == j[1]):
        i = i[1]
        j = j[0]
        # print(i,j)
        return int(i), int(j)
    if(i[1] == j[0]):
        i = i[0]
        j = j[1]
        # print(i,j)
        return int(i), int(j)
    if(i[1] == j[1]):
        i = i[0]
        j = j[0]
        # print(i,j)
        return int(i), int(j)
    
    return 0,0

fractions = []
for i in range(10,100):
    for j in range(i+1,100):
        if i%10 == 0 and j%10 == 0:
            continue
        # print(f"i: {i} j: {j}")
        k,l = cancel_values(i,j)
        if k==0 or l==0:
            continue
        
        if (i/j) == (k/l):
            print(i,j,k,l)
            fractions.append([i,j])
            print(f"fractions: {fractions}")
            break

print(f"fractions: {fractions}")

num = 1
den = 1
for item in fractions:
    num = num * item[0]
    den = den * item[1]

print(num,den)

print(den/num)
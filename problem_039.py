# Date: 2025.07.21
# Answer: 840

import math


results = {}
for a in range (0,500):
    for b in range (a,500):
        c = int(math.sqrt(a**2 + b**2))
        if a**2 + b**2 != c**2:
            continue
        p = a+b+c
        if p > 1000:
            break
        if results.get(p) is not None:
            results[p] += 1
        else:
            results[p] = 1

for item in results:
    print(item,results[item])

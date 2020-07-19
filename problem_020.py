# Date: 2020.07.18
# Answer: 648

import math

num = 100

num_fact = math.factorial(num)
str_num_fact = str(num_fact)
print(num_fact)
sum = 0
for i,value in enumerate(str_num_fact):
    sum += int(value)

print(sum)
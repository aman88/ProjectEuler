# Date: 2025.07.20
# Answer: 1366

import math

power=1000

value = 2
for i in range (2,power+1):
    value= 2*value
print(f"2 to the power of {power} is {value}")

str_num = list(str(value))

sum = 0
for item in str_num:
    sum += int(item)

print(f"The sum of the digits of {value} is {sum}")

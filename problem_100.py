# Date: 2019.11.01
# Answer: 

import math
#print(math.sqrt(13*14))

# n = math.pow(10,12)
# b = math.ceil(math.sqrt(n/2))

# print(b)

#b = 0
# print(math.sqrt(n/2))
# print(math.pow(b,2))
# print(b)
# for i in range(700000,710000):
#     if math.pow(i,2)-i > math.pow(10,12)/2:
#         b=i
#         break
# print(b)
#print(numerator, denominator, numerator/denominator)
b = 0
n = 5#math.pow(10,12)

def next_b(n):
    denominator = math.pow(n,2)-n
    b = math.ceil(math.sqrt(denominator/2))+1
    return b

def next_n(b):
    numerator = math.pow(b,2)-b
    n = math.ceil(math.sqrt(2*numerator))+1
    return n

def validate(b,n):
    numerator = math.pow(b,2)-b
    denominator = math.pow(n,2)-n
    print(numerator, denominator, numerator/denominator)
    return (math.pow(b,2)-b) * 2 == math.pow(n,2)-n


# for i in range(15):
# #while True:
#     if not validate(b,n):
#         if (math.pow(b,2)-b) * 2 > math.pow(n,2)-n:
#             n = next_n(b)
#         else:
#             b = next_b(n)


# #print(validate(85,120))
# import math
# print(math.sqrt(math.pow(10,12)/2))
# print(707106*707105/499998188130)
# print(math.sqrt(499998188130/2))

print(499999*499999)

# Date: 2019.10.31
# Answer: 76576500

import math

def nextTriangle(list):
    # take the last index, increment it
    # take the sum, add to it the last index after being incremented 
    list.append([list[-1][0]+1,list[-1][1]+list[-1][0]+1])
    return list        

def numDivisors(val):
    divisors = set()
    for i in range(1,math.ceil(math.sqrt(val))):
        if val % i == 0:
            divisors.update([i,val/i])
    #print(divisors)
    return len(divisors)

def findTriangle(minDivisors):
    # prime the list
    # index, triangle number, num divisors
    list = [[1, 1, 1]]
    #run loop while num divisors of last index is <= 500
    while list[-1][2] <= minDivisors:
        list = nextTriangle(list) # add the index and triangle number to the list
        list[-1].append(numDivisors(list[-1][1])) # add num divisors for last index to list
        if list[-1][0] % 1000 == 0: 
            print(list[-1])
    return list

print(findTriangle(500)[-1])

# list = [[1, 1, 1]]
# for i in range(10):
#     list = nextTriangle(list)
#     numDivisors(list[-1][1])

# print(list)

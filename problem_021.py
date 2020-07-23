# Date: 2020.07.22
# Answer:31626

import math
# copied from problem 12
def properDivisors(val):
    #returns list of divisors not including itself
    # [values, num of divisors, sum of divisors]
    divisors = {1}
    for i in range(2,math.ceil(math.sqrt(val))):
        if val % i == 0:
            divisors.update([i,val/i])
    #print(divisors)
    #print(val,len(divisors),int(sum(divisors)))
    return [val,len(divisors),int(sum(divisors))]

def check_amicable(val,divList):
    tmp = divList[val][2]
    #print(val,numDivisorsList[tmp][2])
    if(tmp<len(divList) and not(val==tmp)):
        return val == divList[tmp][2]
    return False

def createDivisorsList(upperBound):
    properDivisorsList = [[0,0,-1],[1,1,1]]
    for i in range(2,upperBound+1):
        properDivisorsList.append(properDivisors(i))
    return properDivisorsList

def createAmicableNumsList(inputList):
    amicableNums = []
    for i in inputList:
        if(check_amicable(i[0],inputList)):
            amicableNums.append(i[0])
            #print(i[0])
    return amicableNums


# print(numDivisorsList)
# print(numDivisorsList[220])
# print(numDivisorsList[228])

# print(numDivisorsList[1000][1])
# print(check_amicable(220))
# print(numDivisors(220))

a = createDivisorsList(10000)
#createAmicableNumsList(a)
print(sum(createAmicableNumsList(a)))

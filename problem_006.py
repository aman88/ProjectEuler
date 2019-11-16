import math

def difference_squares(value):
    sum_squares = 0
    sums = 0
    for i in range(1,value+1):
        sum_squares += math.pow(i,2)
        sums += i
    return sum_squares, math.pow(sums,2), math.pow(sums,2)-sum_squares

print(difference_squares(100))

# math.pow(i,2)

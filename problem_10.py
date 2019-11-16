import math

def is_prime(value):
    for i in range(2,math.ceil(math.sqrt(value)+1)):
        if value % i == 0:
            return False
    return True

def next_prime(starting_value):
    value = starting_value
    while(True):
        if value % 2 == 0:
            value += 1
        else:
            value += 2
        if is_prime(value):
            return value

def sum_primes(max_value):
    sum = 2
    current_prime = 2
    while(True):
        next_p = next_prime(current_prime)
        if next_p > max_value:
            break
        current_prime = next_p
        print(current_prime)
        sum += current_prime
    return sum

print(sum_primes(2000000))
        
# Answer: 142913828922
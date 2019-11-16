import math

def is_prime(value):
    for i in range(2,math.ceil(value/2+1)):
        if value % i == 0:
            return False
    return True

def next_prime(starting_value):
    value = starting_value
    while(True):
        value += 1
        if is_prime(value):
            return value

def find_prime(desired_index):
    current_prime = 2
    for i in range(2,desired_index+1):
        current_prime = next_prime(current_prime)
        if i == desired_index:
            return current_prime

    # for i in range(1,prime):
    #     if prime % i != 0:

print(find_prime(10001))
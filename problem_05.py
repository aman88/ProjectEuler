def is_multiple(num,max_divisor):
    for i in range(1,max_divisor+1):
        if num % i != 0:
            return False
    return True

def smallest_multiple(max_divisor):
    multiple = max_divisor #start with the largest divisor
    while(not is_multiple(multiple,max_divisor)): 
        multiple+=max_divisor #increment by largest divisor
    return multiple

print(smallest_multiple(20))


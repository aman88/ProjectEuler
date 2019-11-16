import math
value = 600851475143
#value = 13195

# for i in range(2,math.ceil(value/2)):
#     #print(i)
#     if value % i == 0:
#         factors.append(i)
#         is_prime = True
#         print("factors: ",factors)
#         for j in range(2,math.ceil(i/2)):
#             print(i,j)
#             if i % j == 0:
#                 is_prime = False
#         if is_prime == True:
#             prime_factors.append(i)
#             print("primes: ",prime_factors)

def check_factor(value):
    factors = []
    prime_factors = []
    for i in range(2,math.ceil(value/2)):
        if value % i == 0:
            factors.append(i)
            print(factors)
            if is_prime(i):
                prime_factors.append(i)
                print(prime_factors)
            value = value / i
        if value == 1:
            break
    return factors, prime_factors

def is_prime(value):
    for i in range(2,math.ceil(value/2+1)):
        if value % i == 0:
            return False
    return True

print(check_factor(value))

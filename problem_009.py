import math


a = 1
b = 2
c = 1000 - a - b

def check_triplet(a,b,c):
    return math.pow(a,2) + math.pow(b,2) == math.pow(c,2)

def increment():
    global a,b,c
    if b+2 < c:
        b+=1
        c-=1
    else:
        b = a+2
        a = a+1
        c = 1000 - a - b

while not check_triplet(a,b,c):
    increment()
    print(a,b,c)

print(a+b+c)
print(math.pow(a,2),math.pow(b,2),math.pow(c,2))
print(a*b*c)




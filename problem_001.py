a = 0
sum = 0
while a < 1000:
    if a % 3 == 0:
        sum+=a
    elif a % 5 == 0:
        sum+=a
    print(a)
    a+=1
print("sum: ",sum)
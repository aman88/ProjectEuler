sum = 0
fib_prev = 1
fib_cur = 2
while fib_cur < 4000000:
    if(fib_cur%2==0):
        sum += fib_cur
    temp = fib_cur
    fib_cur = fib_cur + fib_prev
    fib_prev = temp
print(sum)


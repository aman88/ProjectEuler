# Date: 2020.07.20
# Answer: 4782

fib_seq = [1,1,2]
fib_digits = [[1,1,1]]
for cnt,val in enumerate(fib_seq):
    print("Sequence: %s, Value: %s, Num Digits: %s" % (cnt, val, 11111))

def next_fib(fib_seq):
    #fib_seq.append(fib_seq[len(fib_seq)-1]+fib_seq[len(fib_seq)-2])
    tmp = fib_seq[-1]+fib_seq[-2]
    fib_seq.append(tmp)
    if(len(str(tmp)) > fib_digits[-1][2]):
        fib_digits.append([fib_seq.index(tmp)+1,tmp,len(str(tmp))])
        print([fib_seq.index(tmp)+1,len(str(tmp))])
        if(len(str(tmp)) == 1000):
            return True
    return False

status = False
while not(status):
    status = next_fib(fib_seq)
#print(fib_seq)


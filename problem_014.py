# Date: 2019.10.31
# Answer: 837799

#tuple: [starting number, 

def collatz(list):
    if list[-1] == 1:
        return list
    elif list[-1] % 2 == 0:
        list.append(list[-1]/2)
    else:
        list.append(list[-1]*3+1)
    return collatz(list)

#index = 13
#longest = len(collatz([13]))
# print(longest[1])
longest = [0,0]
# print(type(longest[1]))
# print(type(len(longest)))


for i in range(13,1000000):
    if len(collatz([i])) > longest[1]:
        longest[0] = i
        longest[1] = len(collatz([i]))
        print(longest)

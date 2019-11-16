# Date: 2019.10.31
# Answer: 21124

import math

numbers = {1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
"hund":"hundred",
"and":"and",
"thou":"thousand"}

sum = 0
#a = 111
#print(len(numbers.get(1)))
# for i in range(a,a+1):
for i in range(1,1001):
    if i % 100 < 20 and i % 100 > 0:
        #print("0-20")
        sum += len(numbers.get(i%100))
    if i % 100 >= 20:
        #print(">20 tens digit")
        sum += len(numbers.get(math.floor(i%100 - i%10)))
    if i % 100 >= 20 and i % 10 > 0:
        sum += len(numbers.get(i%10))
    if i >= 100 and i < 1000:
        if i % 10 != 0 or i % 100 != 0:
            sum += len(numbers.get("and"))
        #print("hund")
        sum += len(numbers.get(math.floor(i/100)))
        sum += len(numbers.get("hund"))
    if i > 999:
        sum += len(numbers.get("thou"))
        sum += len(numbers.get(1))

print(sum)
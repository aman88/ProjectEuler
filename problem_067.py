# Date: 2020.07.18
# Answer: 7273

import array as ar

triangle = []
# input data from file into array
with open('data/data_067.txt') as data:
    for cnt, line in enumerate(data):
       #print("Line {}: {}".format(cnt, line))
       triangle.insert(cnt,line.strip().split(' '))

#print(triangle[0][0])

length = len(triangle)
#print(triangle[length-1])
for r in range(length-1,-1,-1):
    if r != length-1:
        num_cols = len(triangle[r])
        for c in range(num_cols):
            triangle[r][c] = int(triangle[r][c]) + max(int(triangle[r+1][c]),int(triangle[r+1][c+1]))
            print(triangle[r][c],end=" ")
        print()
    
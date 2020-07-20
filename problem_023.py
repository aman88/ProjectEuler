# Date: 2020.07.19
# Answer: 

# prompt: all integers greater than 28123 can be written as the sum of two abundant numbers
max_int = 28123

def evaluate_abundance(num):
    divisors = []
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            divisors.append(i)
            sum += i
    return num, sum > num

def list_of_abundant_numbers():
    num_list = []
    for i in range(1,max_int+1):
        result = evaluate_abundance(i)
        if result[1]:
            num_list.append(result[0])
            #print(result)
    return num_list

def is_sum_of_two(num,abundant_list):
    for i in abundant_list:
        if num > i:
            #print("here")
            tmp = num - i
            if tmp in abundant_list:
                #print(i)
                return True
    return False
         
abundant = list_of_abundant_numbers()
print("calculated abundant")

sum = 0
for i in range(1,max_int+1):
    if not(is_sum_of_two(i,abundant)):
        #print(i)
        sum += i

print(sum)
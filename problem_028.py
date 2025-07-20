# Date: 2025.07.20
# Answer: 669171001

def top_left(spiral):
    value = 3
    sum = 0
    while value <=spiral:
        sum += ((value*value)-(value-1))
        value += 2
        print(f"{value} {sum}", end="\r")
    print()
    return sum

def top_right(spiral):
    value = 3
    sum = 0
    while value <=spiral:
        sum += (value*value)
        value += 2
        print(f"{value} {sum}", end="\r")
    print()
    return sum

def bot_right(spiral):
    value = 3
    sum = 0
    while value <=spiral:
        sum += (((value-2)*(value-2))+value-1)
        value += 2
        print(f"{value} {sum}", end="\r")
    print()
    return sum

def bot_left(spiral):
    value = 3
    sum = 0
    while value <=spiral:
        sum += (value*value)-(value-1)-(value-1)
        value += 2
        print(f"{value} {sum}", end="\r")
    print()
    return sum


# value = 7
# print(((value-2)*(value-2))+value-1)

spiral = 1001

print(top_left(spiral)+top_right(spiral)+bot_left(spiral)+bot_right(spiral)+1)
# Date: 2020.07.20
# Answer: 9183dddddddddd

terms = set()
print(terms)
print(len(terms))

# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5

for i in range(2,101):
    for k in range(2,101):
        terms.add(i**k)

print(terms)
print(len(terms))
# Date: 2020.07.18
# Answer: 137846528820


# every route must have as many "right" and "down" as the size of the grid
# for example, a 10x10 would need 10 rights and 10 downs

# A permutation with repetition is an arrangement of objects, where some objects are repeated a prescribed number of times.
# formula = n! / (n1! * n2! * n3!...)

import math

grid_size = 20

n = grid_size * 2

num_routes = math.factorial(n) / (math.factorial(grid_size)*math.factorial(grid_size))

print(num_routes)
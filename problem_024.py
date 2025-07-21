# Date: 2025.07.20
# Answer: 2783915460

import math
from itertools import permutations
import time



if __name__ == "__main__":
    start_time = time.perf_counter()

    list_perms = list(permutations([0,1,2,3,4,5,6,7,8,9]))

    print(len(list_perms))


    print(list_perms[1000000-1])
    
    cur_time = time.perf_counter()
    elapsed_time = cur_time - start_time
    print(f"Function execution time: {elapsed_time:.6f} seconds")
        

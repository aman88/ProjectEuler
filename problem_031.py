# Date: 2025.07.20
# Answer: 73682

import time

start_time = time.perf_counter()

i=j=k=l=m=n=o=p=0
num_combinations = 0
for i in range(201):
    for j in range(101):
        if(1*i+2*j > 200):
            continue
        for k in range(41):
            if((i+k) % 2 != 0):
                continue
            if(1*i+2*j+5*k > 200):
                    continue
            for l in range(21):
                if(1*i+2*j+5*k+10*l > 200):
                    continue
                for m in range(11):
                    for n in range(5):
                        for o in range(3):
                            for p in range(2):
                                if(1*i+2*j+5*k+10*l+20*m+50*n+100*o+200*p == 200):
                                    num_combinations += 1
                                    if(num_combinations%5000==0):
                                        print("\n")
                                        print(num_combinations)
                                        print(i,j,k,l,m,n,o,p)
                                        cur_time = time.perf_counter()
                                        elapsed_time = cur_time - start_time
                                        print(f"Function execution time: {elapsed_time:.6f} seconds")

print("\nEnd result")
print(num_combinations)
print(i,j,k,l,m,n,o,p)
cur_time = time.perf_counter()
elapsed_time = cur_time - start_time
print(f"Function execution time: {elapsed_time:.6f} seconds")

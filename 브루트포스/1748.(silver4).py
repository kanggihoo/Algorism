
import math
N = int(input())
len_N = len(str(N))
total = 0
idx = 0

for i in range(1,len_N+1):
    if i == len_N:
        count = N - 10**(i-1)+1
        total += count*i
    else:
        total += (10**i - 10**(i-1))*i

print(total)
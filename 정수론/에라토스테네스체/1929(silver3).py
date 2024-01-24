# 소수 구하기
import math
M , N = map(int , input().split())
arr = [i if i > 1 else 0 for i in range(N+1)]

# 소수 찾기
for i in range(2,int(math.sqrt(N))+1):
    if arr[i] == 0:
        continue
    j = 2
    while(j*i <= N):
        arr[i*j] = 0
        j+=1

# 소수 출력
for i in range(M,N+1):
    if arr[i] !=0:
        print(i)

    

            
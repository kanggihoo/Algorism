# 1644 연속된 소수의 합
import math
N = int(input())
check = [True for _ in range(N+1)] 
count = 0
for i in range(2,int(math.sqrt(N))+1):
    for j in range(i+i, N+1, i):
        if not check[i]:
            break
        check[j] = False

prime = []
for i in range(2,N+1):
    if check[i]:
        prime.append(i)
if not len(prime):
    print(0)
else:
    result = 0 
    acc_sum = prime[0]
    L , R = 0,0
    # print(prime)
    while L <= R:
        # 2 3 5 7
        if acc_sum < N:
            R +=1
            if R < len(prime):
                acc_sum += prime[R]
            else:
                break
        elif acc_sum > N:
            acc_sum -= prime[L]
            L +=1
        else:
            result +=1
            acc_sum -= prime[L]
            L +=1
    print(result)
        
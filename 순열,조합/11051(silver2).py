# 자연수 N , 정수 K가 주어질 때 이항계수 (N,K) 구하시오
from itertools import combinations , permutations

N , K = map(int , input().split())

D = [[0]*(K+2) for _ in range(N+1)]
# 초기화 K = 0 일때는 무조건 0 , K=1일때는 무조건 n
for i in range(1,N+1):
    D[i][0] = 1
    D[i][1] = i

if N >=2:
    for i in range(2,N+1):
        for j in range(2,K+1):
            D[i][j] = (D[i-1][j]%10007 + D[i-1][j-1]%10007)%10007


print(D[N][K])

# count = 0
# for i in combinations(list(range(N)),K):
#     count +=1


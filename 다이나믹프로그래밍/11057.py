
N = int(input())
D = [[1]*10 for _ in range(N+1)]

# 초기화 

#
for i in range(2,N+1):
    for j in range(10):
        D[i][j] = sum(D[i-1][k] for k in range(j+1)) % 10007
print(sum(D[N]) % 10007)

N = int(input())
A = list(map(int , input().split()))
D = [1 for i in range(N)]
D[0] = 1

for i in range(1,N):
    tmp = [D[k] for k in range(i) if A[k] < A[i]]
    if tmp :
        D[i] = max(tmp) +1

print(max(D))

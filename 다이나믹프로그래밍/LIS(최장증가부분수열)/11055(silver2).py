'''
증가하는 부분 수열 중 합이 가장 큰 경우
'''

N = int(input())
A = list(map(int , input().split()))
D = [A[i] for i in range(N)]
for i in range(1,N):
    tmp = [D[k] for k in range(i) if A[k] < A[i]]
    if tmp :
        D[i] = max(tmp)+A[i]
# print(D)
print(max(D))

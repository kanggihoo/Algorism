'''
가장 긴 증가하는 부분 수열의 길이 출력
'''
import heapq
HQ = []
N = int(input())
A = list(map(int , input().split()))
D = [A[i] for i in range(N)]
max_length = 0
for i in range(1,N):
    tmp = [D[k] for k in range(i) if A[k] < A[i]]
    if tmp :
        D[i] = max(tmp)+A[i]
# print(D)
print(max(D))

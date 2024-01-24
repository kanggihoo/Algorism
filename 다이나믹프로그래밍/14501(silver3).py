'''


'''
import sys
input = sys.stdin.readline
N = int(input())
D = [0 for i in range(2+N)]
P = [0 for i in range(2+N)]
T = [0 for i in range(2+N)]
for i in range(1,N+1):
    Ti , Pi = map(int , input().split())
    T[i] , P[i] = Ti , Pi

for i in reversed(range(1,N+1)):
    if i+T[i] > N+1:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1] , D[i+T[i]]+P[i])
print(D[1])


    
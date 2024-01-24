import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)
for i in range(1,N+1):
    T[i] , P[i] = map(int , input().split())

D = [0]*(N+1)
Result = 0

for i in range(1,N+1):
    





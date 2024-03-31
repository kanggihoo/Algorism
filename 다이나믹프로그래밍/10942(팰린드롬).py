import sys
input = sys.stdin.readline
N = int(input())
array =[-1]+ list(map(int , input().split()))

D = [[0]*(N+1) for _ in range(N+1)]
# D[S][E] => S~E가 팰린드롬이면 1 아니면 0 
'''
    1. S[i] == S[i+1] 이면 D[i][i+1] == 1
    2. if S[i] == S[j] and D[i+1][j-1] == 1 이면 D[i][j] = 1 
'''
# 대각원소 초기화(S==E인 경우는 항상 1)
for i in range(1,N+1):
    D[i][i] = 1
# S+1 == E인 경우 초기화(서로 인접한 경우)
for i in range(1,N):
    if array[i] == array[i+1]:
        D[i][i+1] =1
# # i, j 모든 경우 조사 (2칸 이상 떨어진 경우)
'''
=> dist가 2일때 start 점을 움직며 가능한 곳을 탐색 후 dist를 증가시켜야됨
=> 반대로 start 고정상태에서 dist 2 , 3,,, 으로 탐색하면 부분문제가 아니게됨
=> 즉 for문의 누가 먼저 순환할 것인지를 명확하게 해야함
'''
for dist in range(2,N):
    for start in range(1,N+1-dist):
        end = start +dist
        if array[start] == array[end] and D[start+1][end-1] == 1:
            D[start][end] = 1

M = int(input())
for _ in range(M):
    s ,e = map(int , input().split())
    print(D[s][e])




            
            
            
     
    

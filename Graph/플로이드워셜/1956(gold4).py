import math
import sys
INF = math.inf
input = sys.stdin.readline
N, M = map(int , input().split())

graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    n1, n2 , c = map(int , input().split())
    graph[n1][n2] = c
    

# 플로이도 워샬 알고리즘
for t in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j] , graph[i][t] + graph[t][j])

cycle_min = INF
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            continue
        if graph[i][j] != INF and graph[j][i] != INF:
            cycle_min = min(cycle_min ,  graph[i][j] + graph[j][i])    
if cycle_min == INF:
    print(-1)
else:
    print(cycle_min)
    
    

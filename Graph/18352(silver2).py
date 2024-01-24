# 1~N개의 노드, M개의 간선(단방향), 간선 가중치 : 1
# 특정 도시 X번 노드에서 출발해서 도달가능한 모든 도시 중 최단 거리가 K인 모든 도시의 번호 출력(오름차순)
# 만약 최단 거리가 K인 도시가 없으면 -1출력

import sys
from collections import deque
input = sys.stdin.readline
N , E , K , X = map(int , input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
depth_arr = [0 for _ in range(N+1)]
result = []
# 간선 입력 받은 후 그래프 만들기
for _ in range(E):
    n1 , n2 = map(int , input().split())
    graph[n1].append(n2)

# 너비 우선 탐색 (BFS)
Q = deque()
depth = 1 # depth가 K가 되어야 함

# 첫번째 노드 대입
Q.append(X)
visited[X] = True
depth_arr[X] = 0
while Q:
    node = Q.popleft()
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            depth_arr[i] = depth_arr[node]+1
            Q.append(i)
            if depth_arr[i] ==K:
                result.append(i)
    
   

# while문이 depth ==K 여서 종료되었는지 확인

if len(result):
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
    


    
    

    



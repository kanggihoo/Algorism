# 0 : R , 1 :B
from collections import deque
def bfs(state,visited):
    for i in range(1,V+1):
        if visited[i] ==-1:
            Q = deque()
            Q.append((i,state))
            visited[i] = state
            while Q:
                cur , cur_state = Q.popleft()
                next_state = 0 if cur_state == 1 else 1         
                for adj in graph[cur]:
                    if visited[adj] == cur_state:
                        return False
                    elif visited[adj] ==-1:
                        Q.append((adj,next_state))
                        visited[adj] = next_state
    return True
import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V,E = map(int , input().split())
    graph = [[]for _ in range(V+1)]
    visited = [-1 for _ in range(V+1)]
    for _ in range(E):
        n1,n2 = map(int , input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    if bfs(0,visited):
        print("YES")
    else:
        print("NO")


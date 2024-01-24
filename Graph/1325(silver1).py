# N개의 컴퓨터, 
# A개 B를 신뢰할 떄 A를 해킹하면 B도 해킹가능
# 신뢰관계가 주어졌을 때 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호 출력

# 출력할 때 해킹할 수 있는 컴퓨터 번호를 오름차순으로 출력

# BFS도 되지 않나? 깊이추가해서

## pypy3에서는 맞는데 python3에서는 시간초과 뜨냐
import sys
from collections import deque
input = sys.stdin.readline

N , M = map(int , input().split())
confidence = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
# 그래프 만들기
for _ in range(M):
    n1 , n2 = map(int , input().split())
    graph[n1].append(n2)
    

def BFS(start):
    visited = [False for _ in range(N+1)]
    Q = deque()
    Q.append(start)
    visited[start] = True

    while Q:
        node = Q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                confidence[i] +=1
                Q.append(i)
    
    # print(f"start : {start} , distance = {confidence}")
    
# 모든 느드에 대하여 BFS
for node in range(1,N+1):
    BFS(node)

# 신뢰도를 바탕으로 가장 높은 신뢰도 출력
max_confidence = max(confidence)
for node in range(1,N+1):
    if confidence[node] == max_confidence:
        print(node , end=' ')
        
    
    
    
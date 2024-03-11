# 방향 그래프와 시작점이 주어지면
# 시작점으로 부터 모든 정점으로의 최단 경로 구하는 코드 작성

from queue import PriorityQueue
import math
import sys
input = sys.stdin.readline
V , E = map(int , input().split())
S = int(input())
graph = [[] for _ in range(V+1)]

# 그래프 초기화

for _ in range(E):
    n1 , n2 , cost = map(int , input().split())
    graph[n1].append((n2,cost))
INF = math.inf
distacne = [INF for _ in range(V+1)]
visited = [False for _ in range(V+1)]


# 다익스트라 시작
distacne[S] = 0
PQ = PriorityQueue()
PQ.put((distacne[S] , S))


# 출발 노드 부터 모든 노드 까지의 최단 거리계산
while not PQ.empty():
    
    now_cost , now_node = PQ.get() # 큐에 들어 있는 값들 중 distance 값이 가장 작은 것이 우선적으로 빠짐
    if distacne[now_node] == INF: # 큐에서 나온적이 있는 노드인경우 pass
        continue
    # visited[now_node] = True
    
    # 현재 노드에 인접한 모든 노드 검사 
    for next_node , next_cost in graph[now_node]:
        tmp = now_cost + next_cost
        # 현재 저장된 다음 노드의 거리 값이 현재 노드와 가중치 합보다 작은경우는 pass
        if tmp > distacne[next_node]:
            continue
        distacne[next_node] = tmp
        # 다음 노드의 거리값과, 다음 노드 번호를 우선순위 큐에 넣은 뒤 우선순위 큐에서는 거리값이 가장 작은것을
        # 우선적으로 가져온다.
        PQ.put((tmp , next_node))


# 출발점으로 부터 떨어진 모두 노드와의 최단거리 출력
for i in range(1,V+1):
    if distacne[i] == INF:
        print("INF")
    else:
        print(distacne[i])
        
        



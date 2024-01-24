# N개의 도시, M개의 버스
# A번째 도시에서 B번째 도시까지 가는 데 드는 최소비용출력
# 도시 번호는 1~None
import sys
import heapq
import math
input = sys.stdin.readline
N  =int(input()) # 도시 개수
M = int(input()) # 간선 개수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1 , n2 , cost = map(int , input().split())
    graph[n1].append((n2 , cost))
    
S , E = map(int , input().split())

INF = math.inf
distance = [ INF for i in range(N+1)]
visited = [ False for i in range(N+1)]
hq = []

# 시작점 초기화
distance[S] = 0
heapq.heappush(hq , (distance[S] , S))

# 최단 경로 계산
while hq:
    
    # 우선순위 큐에서 가져옴. 
    now_cost,now_node  =heapq.heappop(hq)
    
    # 큐에서 나온적 있는지 확인
    if visited[now_node]:
        continue
    visited[now_node] = True
    
    # 인접노드 검사
    for next_node , next_cost in graph[now_node]:
        # 현재 노드 부터 다음 노드까지 거리 계산
        tmp = now_cost + next_cost
        
        if distance[next_node] < tmp:
            continue
        
        distance[next_node] = tmp
        heapq.heappush(hq , (tmp , next_node))
    
print(distance[E])
        

    
    

'''
1->N노드로 이동할 때 특정노드 2개 v1 , v2는 반드시 지나면서 최단거리 구하기
(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

2. 임의의 정점 u,v 사이에 간선이 최대 1개 존재 (간선이 없을 수도 있음)

1) 1->v1 최소비용 + v2->N 최소비용 + v1->v2 최소비용
2) 1->v2 최소비용 + v1->N 최소비용 + v2->v1 최소비용

'''
import sys
import heapq
import math
input = sys.stdin.readline
N , E = map(int , input().split())
# 출발, 도착 노드 
start , end = 1 , N
graph = [[] for _ in range(N+1)]
# 그래프 입력(양방향 그래프)
for _ in range(E):
    n1 , n2 , cost = map(int , input().split())
    graph[n1].append((n2,cost))
    graph[n2].append((n1,cost))
# 반드시 지나야 하는 노드 
v1 , v2 = map(int , input().split())
INF = math.inf
# 시작노드 초기화
def dickstra(S):
    # 거리정보, 방문여부 확인
    
    distance = [INF for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    q = []
    distance[S] = 0
    heapq.heappush(q, (distance[S] , S))

    # 시작노드에 대한 다익스트라 진행
    while q:
        cur_dist , cur_node = heapq.heappop(q) # 현재 거리정보가 가장 작은 것을 우선적으로 pop
        
        # 이미 방문한 노드인지 확인
        if visited[cur_node]:
            continue
        
        visited[cur_node] = True
        # 인접노드 검사
        for adj_node , cost in graph[cur_node]:
            tmp = cur_dist + cost
            if distance[adj_node] > tmp:
                distance[adj_node] = tmp
                # q에 집어넣기
                heapq.heappush(q, (distance[adj_node] , adj_node))
    return distance

distance_S = dickstra(start)
distance_v1 = dickstra(v1)
distance_v2 = dickstra(v2)
# print(distance_S)
# print(distance_v1)
# print(distance_v2)
## 예외처리
'''
1. v1->v2 간의 간선이 없는 경우 
2. S->v1 또는 v2->E 간선 없는 경우
3. S->v2 또는 v1->E 간선 없는 경우
'''
if distance_v1[v2] == INF:
    print(-1)
else:
    # case 1(s->v1 + v2->end) + v1->v2 
    case1 = distance_S[v1] + distance_v2[end] + distance_v1[v2]
    # case 2(s->v2 + v1->end) + v1->v2
    case2 = distance_S[v2] + distance_v1[end] + distance_v1[v2]

    # case1 == case2가 모두 INF 인경우는 v1,v2를 반드시 지나서 갈 수 없는 경우
    if case1 == INF and case2 == INF:
        print(-1)
    else:
        print(min(case1 , case2))





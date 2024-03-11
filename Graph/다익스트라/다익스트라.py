import sys
import math
input = sys.stdin.readline
INF = math.inf


########################################################################################### O(V^2) 다익스트라 알고리즘

# # 노드의 개수, 간선의 개수 입력
# N , E = map(int, input().split())
# # 시작 노드 번호
# S = int(input())
# # 각노드에 연결되어 있는 노드 정보
# graph = [[] for _ in range(N+1)]

# # 방문한 적 있는지 체크
# visited = [ False for _ in range(N+1)]

# # 최단 거리 테이블 모두 INF로 초기화
# distance = [INF for _ in range(N+1)]

# # 간선 정보 입력받기
# for _ in range(E):
#     n1, n2 , cost = map(int , input().split())
#     graph[n1].append((n2,cost))

# # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallist_node():
#     min_value = INF
#     min_index = None
#     for i in range(1,N+1):
#         if i == S:
#             continue
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             min_index = i
#     return min_index            
            
            

# def dijkstra(start):
#     # 시작 노드에 대한 초기화
#     distance[start] = 0
#     visited[start] = True
#     for node,cost in graph[start]:
#         distance[node] = cost
        
#     # 시작 노드 제외 N-1개의 노드에 대해 반복
#     for i in range(N-1):
#         now = get_smallist_node()
        
#         visited[now] = True
#         for j , cost in graph[now]:
#             tmp_cost = distance[now] + cost
            
#             if tmp_cost < distance[j]:
#                 distance[j] = tmp_cost

# dijkstra(S)

# # 모든 노드로 가기 위한 최단 거리 출력
# for i in range(1, N+1):
#     if distance[i] == INF:
#         print("start -> {} is INFINITY".format(i))
#     else:
#         print("start -> {} : {}".format(i , distance[i]))

            
        
            
    
########################################################################################### O(ElogV) 다익스트라 알고리즘
import heapq
# 노드의 개수, 간선의 개수 입력
N , E = map(int, input().split())
# 시작 노드 번호
S = int(input())
# 각노드에 연결되어 있는 노드 정보
graph = [[] for _ in range(N+1)]

# 방문한 적 있는지 체크
visited = [ False for _ in range(N+1)]

# 최단 거리 테이블 모두 INF로 초기화
distance = [INF for _ in range(N+1)]

# 간선 정보 입력받기
for _ in range(E):
    n1, n2 , cost = map(int , input().split())
    graph[n1].append((n2,cost))
   
                    

def dijkstra(start):
    # 시작 노드에 대한 초기화
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        
        ccost , now = heapq.heappop(q)
        if distance[now] == INF:
            continue
        
        for j , cost in graph[now]:
            tmp_cost = ccost + cost
            
            if tmp_cost < distance[j]:
                distance[j] = tmp_cost
                heapq.heappush(q , (distance[j] , j))

dijkstra(S)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N+1):
    if distance[i] == INF:
        print("start -> {} is INFINITY".format(i))
    else:
        print("start -> {} : {}".format(i , distance[i]))
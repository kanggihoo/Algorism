'''
N개의 숫자 구분된 마을에 한명의 학생 거주
N명의 학생이 i번 마을에 모임. 
마을에는 M개의 단방향 도로존재, 각 도로마다 소요시간 있음
각 학생은 해당마을로 이동 후 다시 자기 마을로 돌아와야함. 이때 최단시간
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구인지 구하라
'''
import sys
import heapq
input = sys.stdin.readline
N , M ,X = map(int , input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1,n2,cost = map(int , input().split())
    graph[n1].append((n2,cost))
import math
INF = math.inf
def dick(start):
    visited = [False for _ in range(N+1)]
    distance = [INF]*(N+1)
    distance[start] = 0
    HQ = []
    heapq.heappush(HQ , (distance[start] , start))
    while HQ:
        ccost , cnode = heapq.heappop(HQ)
        if visited[cnode]:
            continue
        visited[cnode] = True
        for adj , w in graph[cnode]:
            tmp = distance[cnode]+w
            if distance[adj] > tmp:
                distance[adj] = tmp
                heapq.heappush(HQ , (distance[adj] , adj))
    return distance
node_to_X = [0]*(N+1)            
for i in range(1,N+1):
    if i == X:
        continue
    node_to_X[i] = dick(i)[X]

X_to_node = dick(X)

for i in range(1,N+1):
    X_to_node[i] += node_to_X[i]
print(max(X_to_node[1:]))
        

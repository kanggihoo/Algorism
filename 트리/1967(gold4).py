# 트리 지름 구하기 => 아무 노드에서 출발해서 가장 긴 거리를 가진 노드를 구한뒤, 구한 노드에서 부터 가장 멀리 떨어진 거리가
# 트리의 지름이 된다.
'''
1967.py
1번 ~N번 노드
부모 노드 , 자식 노드 , 가중치
루트 노드는 항상 1
'''
import sys
input = sys.stdin.readline
N = int(input())       
graphs = [[] for _ in range(N+1)]
for i in range(N):
    inputs = list(map(int , input().split()))
    node = inputs[0]
    for i in range(1,len(inputs)-1,2):
        graphs[node].append((inputs[i] , inputs[i+1]))
    


from collections import deque 
def bfs(start):
    result = {"max_distance" : 0 , "max_node" : 0}
    Q = deque()
    Q.append((start,0))
    visited = [False for _ in range(N+1)]
    visited[start] = True
    while Q:
        cur_node , cur_cost = Q.popleft()
        
        for adj , C in graphs[cur_node]:
            if not visited[adj]:
                visited[adj]=True
                Q.append((adj,cur_cost+C))
                if result["max_distance"] < cur_cost+C:
                    result["max_distance"] = cur_cost+C
                    result["max_node"] = adj
    return result

root = 1
result = bfs(1)
result = bfs(result["max_node"])
print(result["max_distance"])


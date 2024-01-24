'''
트리의 부모 찾기
- 트리의 루트 노드는 항상 1이다.
'''


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
parents = [None for _ in range(N+1)]

for _ in range(N-1):
    n1 , n2 = map(int , input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
def bfs(s , visited , parents):
    
    visited[s] = True
    for adj in graph[s]:
        if not visited[adj]:
            bfs(adj , visited , parents)
            parents[adj] = s
    
bfs(1 , visited , parents)
for i in parents[2:]:
    print(i)
    
    
    
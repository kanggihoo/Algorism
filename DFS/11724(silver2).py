import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N ,M = map(int , input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int , input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def BFS(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            BFS(i)
     
num = 0

for i in range(1,N+1):
    if not visited[i]:
        BFS(i)
        num +=1
        
print(num)
        
    

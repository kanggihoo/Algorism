graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*(len(graph))

def DFS(graph , start , visited):
    print(start , end ='')
    if not visited[start]:
        visited[start] = True
        
        for node in graph[start]:
            if not visited[node]:
                DFS(graph, node , visited)
                
from collections import deque
def BFS(graph, start , visited):
    visited[start] = True
    Q = deque(  )
    print(start , end='')
    while Q:
        node = Q.popleft()
        visited[node] =True
        print(node,end='')
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                Q.append(i)
                
BFS(graph,1,visited)
print(visited)
            
        
    
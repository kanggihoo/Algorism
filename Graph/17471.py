N = int(input())
P = [0]+list(map(int , input().split()))
graph = [[] for i in range(N+1)]
# print(graph)
for i in range(1,N+1):
    nodes = list(map(int , input().split()))
    for j in range(1,len(nodes)):
        node = nodes[j]

        graph[i].append(node)
from collections import deque
def bfs(nodes):
    Q = deque()
    Q.append(nodes[0])
    visited = [False for _ in range(N+1)]
    visited[nodes[0]] = True
    count = 1
    while Q:
        cn = Q.popleft()
        for adj in graph[cn]:
            if not visited[adj] and adj in nodes:
                Q.append(adj)
                visited[adj] = True
                count +=1
    return True if count == len(nodes) else False
    
    
ans = int(1e4)
def find_com(idx, result):
    if len(result) >=1:
        # 연결이되어 있는지 확인 후 최소 최소 비교
        nodes1 = result 
        nodes2 = [i for i in range(1,N+1) if i not in result]
        if bfs(nodes1) and bfs(nodes2):
            b1 = bfs(nodes1)
            b2 = bfs(nodes2)
            # print(b1,b2)
            # print(nodes1 , nodes2)
            global ans 
            s1 = sum(P[i] for i in nodes1)
            s2 = sum(P[i] for i in nodes2)
            ans = min(ans , abs(s1-s2))
            

    if len(result) == N//2:
        return 
    # print(result)    
    for j in range(idx+1,N+1):
        find_com(j,result+[j])

find_com(0,[])
if ans == int(1e4):
    print(-1)
else:
    print(ans)
# print(graph)
# print(bfs([4,5]))
# print(bfs([1,2,3,5]))

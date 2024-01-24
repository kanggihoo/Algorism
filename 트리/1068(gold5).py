'''
리프 노드 개수 구하기

0번 노드부터 N-1번 노드까지 각 노드의 부모가 주어짐
(부모가 없다면 -1이 주어짐)
지울 노드의 번호가 주어지고 리프 노드의 개수 출력
'''
import sys
input = sys.stdin.readline
N = int(input())
trees = list(map(int , input().split()))
remove = int(input())

graph = [[]for _ in range(N)]
root = None
visited = [False for _ in range(N)]
result = 0
for i in range(len(trees)):
    if trees[i] != -1:
        graph[i].append(trees[i])
        graph[trees[i]].append(i)
    else:
        root = i


## 루트부터 출발 
from collections import deque
Q = deque()
if root != remove:
    Q.append(root)
visited[root] = True
while Q:
    cur = Q.popleft()
    
    cnode = 0 
    for adj in graph[cur]:
        if not visited[adj] and adj != remove:
            cnode +=1
            Q.append(adj)
            visited[adj] = True
    if cnode == 0:
        result +=1
print(result)
            






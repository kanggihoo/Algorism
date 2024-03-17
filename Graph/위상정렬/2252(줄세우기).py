import sys
input = sys.stdin.readline

N , M =map(int , input().split())
G = [[] for _ in range(N+1)]
degrees = [0]*(N+1)
for _ in range(M):
    n1,n2 = map(int , input().split())
    G[n1].append(n2)
    degrees[n2] +=1

from collections import deque
Q = deque()
for idx,n in enumerate(degrees[1:],1):
    if n == 0:
        Q.append(idx)
while Q:
    cur = Q.popleft()
    print(cur)
    for adj in G[cur]:
        degrees[adj] -=1
        # print("cur : " , cur , "adj:" , adj)
        if degrees[adj] ==0:
            Q.append(adj)
        
    
    
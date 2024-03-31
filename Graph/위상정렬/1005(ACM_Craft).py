import sys
input = sys.stdin.readline

from collections import deque
def bfs(target):
    Q = deque()
    # Q 초기화
    for idx  in range(1,N+1):
        if degrees[idx] == 0:
            Q.append((idx , RT[idx]))
            min_time[idx] = RT[idx]
    while Q:
        cn , ctime = Q.popleft()
        if cn == target:
            return 
        
        for nn in G[cn]:
            degrees[nn] -=1
            min_time[nn] = max(min_time[nn] , ctime+RT[nn]) 
            if degrees[nn] ==0:
                Q.append((nn , min_time[nn]))


T = int(input())
for _ in range(T):
    N , K = map(int , input().split())
    RT = [0]+list(map(int , input().split()))
    G = [[] for _ in range(N+1)]
    degrees = [0]*(N+1)
    for _ in range(K):
        X,Y = map(int , input().split())
        G[X].append(Y)
        degrees[Y]+=1
    min_time = [-1] * (N+1)
    target = int(input())
    bfs(target)
    print(min_time[target])

            
            
            
            
     
    

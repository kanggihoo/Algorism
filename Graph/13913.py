'''
숨박꼭질 4


'''
from collections import deque
N , K = map(int , input().split())
visited = [False]*(100000+1)
Q = deque()
Q.append((N,0))
visited[N] = True
dist = [0]*(100000+1)
dist[N] = N
def move(cx,time):
    path = [cx]
    for i in range(time):
        pre = dist[cx]
        path.append(pre)
        cx = pre
    print(" ".join(list(map(str ,path[::-1]))))
        
while Q:
    cx , time = Q.popleft()
    if cx == K:
        print(time)
        move(cx,time)
        break
    for i in [cx+1 , cx-1 , 2*cx]:
        nx = i
        if 0<=nx<=100000 and not visited[nx]:
            visited[nx] = True
            dist[nx] = cx
            Q.append((nx,time+1))
    
    
    
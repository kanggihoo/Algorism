import sys
input = sys.stdin.readline

from collections import deque
    
'''
1~K개의 바이러스 
1초마다 증식, 번호가 낮은게 먼저 증식, 이때 특정 칸에 이미 존재하면 침투못함
S초 지난 후 바이러스 종류 출력, 해당 위치에 없으면 0출력 
좌 상단이 (1,1)

'''

N ,K = map(int , input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int , input().split())))
S, Y,X = map(int , input().split())
# x,y -1씩 해야함

V =[[] for _ in range(K+1)]

def init(V):
    for i in range(N):
        for j in range(N):
            v = MAP[i][j] 
            if v != 0:
                V[v].append((i,j))
def bfs(V):
    Q = deque()   
    visited = [[False]*N for _ in range(N)]
    for idx ,v in  enumerate(V):
        for y,x in v:
            Q.append((y,x,idx,0))
            visited[y][x] = True
    while Q:
        cy,cx,v,t = Q.popleft()
        if t == S:
            return
        for ny,nx in [(cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)]:
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and MAP[ny][nx] ==0:
                MAP[ny][nx] = v
                visited[ny][nx] = True
                Q.append((ny,nx,v,t+1))
                
init(V)
bfs(V)
# for i in range(N):
#     for j in range(N):
#         print(MAP[i][j] , end= " ")
#     print()
print(MAP[Y-1][X-1])
    


    
            
        
        
    


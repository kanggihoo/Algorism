'''
보물섬 지도 (L:육지 , W:바다)
이동시 상하좌우 및 육지로만 이동
한 칸 이동시 1시간 소요
보물은 두 지점의 거리가 가장 멀리 떨어진 육지 두곳에 묻힘

'''

N , M = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(input().strip()))
from collections import deque

def check(visited):
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and maps[i][j] =="L":
                return (i,j)
    return None

def bfs(y,x,visited,step=0):
    Q = deque()
    Q.append((y,x,0))
    visited[y][x] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    dist = 0
    tmp = [(y,x,0)]
    while Q:
        cy,cx,depth = Q.popleft()
        dist = max(dist , depth)
        for ddy ,ddx in zip(dy,dx):
            ny ,nx = ddy+cy , ddx+cx
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and maps[ny][nx]=="L":
                Q.append((ny,nx,depth+1))
                tmp.append((ny,nx,depth+1))
                visited[ny][nx] = True
    if step ==0:
        return [i[:2] for i in tmp if i[2] == dist]
    else:
        return dist

visited = [[False]*M for _ in range(N)]
# 각 그룹별 임의 점에서 가장 멀리 떨어진 모든 점 찾기
candidates = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == "L" and not visited[i][j]:
            candidates.append(bfs(i,j,visited,0))
visited = [[False]*M for _ in range(N)]
max_dist = 0
# print(candidates)
for group in candidates:
    max_dist = max (bfs(*group[0] , visited,step=1) , max_dist)

print(max_dist)
        
        
    
    
    
    


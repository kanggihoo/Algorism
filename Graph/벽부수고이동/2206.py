# 현재 경로에서 벽을 통과하되 딱 1번만 부수고 간 모든 경로중 최단 경로 
N , M = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input())))
    
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx =[0,0,1,-1]
dy =[1,-1,0,0]

from collections import deque

def bfs():
    Q = deque()
    Q.append((0,0,0)) # y, x , 벽파괴여부 (0이면 파괴않함, 1이면 파괴했음)
    visited[0][0][0] = 1 # 초기위치도 최단거리에 반영

    while Q:
        y,x,wall = Q.popleft()
        if y==N-1 and x ==M-1:
            return visited[y][x][wall]
        for ddy ,ddx in zip(dy,dx):
            ny,nx = ddy+y,ddx+x 
            if 0<=ny<N and 0<=nx<M and visited[ny][nx][wall]==0: # 한번도 방문한적이 없는 경우 
                # 다음위치가 벽이 아닌경우
                if maps[ny][nx] ==0:
                    Q.append((ny,nx,wall))
                    visited[ny][nx][wall] = visited[y][x][wall]+1
                # 다음위치가 벽인 경우 , 벽을 부순적이 없는 경우 진행
                elif maps[ny][nx] == 1 and wall ==0:
                    Q.append((ny,nx,1))
                    visited[ny][nx][wall+1] = visited[y][x][wall] +1
    return -1   
    
print(bfs())

# for i in range(N):
#         for j in range(M):
#             print(visited[i][j][0] , end =" ")
#         print()
# for i in range(N):
#     for j in range(M):
#         print(visited[i][j][1] , end =" ")
#     print()
            
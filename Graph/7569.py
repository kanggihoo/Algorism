import sys
input = sys.stdin.readline
M , N, H = map(int , input().split())
Boxes = [[] for _ in range(H)]

for i in range(H):
    for _ in range(N):
        Boxes[i].append(list(map(int , input().split())))
# 토마토 위치 찾기

from collections import deque
Q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if Boxes[h][i][j] == 1:
                Q.append((i,j,h,0))
# check함수
def check(Boxes):
    for h in range(len(Boxes)):
        for i in range(len(Boxes[0])):
            for j in range(len(Boxes[0][0])):
                if Boxes[h][i][j] == -1:
                    continue
                if Boxes[h][i][j] == 0:
                    return False
    return True
if len(Q):
    result = 0
    dx =[-1,1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dh = [0,0,0,0,1,-1]
    while Q:
        cur_y,cur_x,cur_h,day = Q.popleft()
        
        for ddx , ddy,ddh in zip(dx,dy,dh):
            nx , ny,nh = cur_x+ddx , cur_y+ddy , cur_h+ddh
            if nx >=0 and nx < M and ny >=0 and ny < N and nh>=0 and nh <H and Boxes[nh][ny][nx] ==0:
                Q.append((ny,nx,nh,day+1))
                Boxes[nh][ny][nx] = 1
                result = day+1                
    # 모든 토마토가 익었는지 확인
    if check(Boxes):
        print(result)
    else:
        print(-1)
else:
    print(-1)
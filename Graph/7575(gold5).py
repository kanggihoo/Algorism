import sys
input = sys.stdin.readline
M , N = map(int , input().split())
Boxes = []
for _ in range(N):
    Boxes.append(list(map(int , input().split())))
# 토마토 위치 찾기

from collections import deque
Q = deque()
for i in range(N):
    for j in range(M):
        if Boxes[i][j] == 1:
            Q.append((i,j,0))
# check함수
def check(Boxes):
    for i in range(len(Boxes)):
        for j in range(len(Boxes[0])):
            if Boxes[i][j] == -1:
                continue
            if Boxes[i][j] == 0:
                return False
    return True
if len(Q):
    result = 0
    dx =[-1,1,0,0]
    dy = [0,0,1,-1]
    
    while Q:
        cur_y,cur_x,day = Q.popleft()
        
        for ddx , ddy in zip(dx,dy):
            nx , ny = cur_x+ddx , cur_y+ddy
            if nx >=0 and nx < M and ny >=0 and ny < N and Boxes[ny][nx] ==0:
                Q.append((ny,nx,day+1))
                Boxes[ny][nx] = 1
                result = day+1                
    # 모든 토마토가 익었는지 확인
    if check(Boxes):
        print(result)
    else:
        print(-1)
else:
    print(-1)
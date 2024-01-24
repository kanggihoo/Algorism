'''
16236 아기상어 문제 
NXN 공간 , M마리 물고기 1마리 상어, 각 칸에는 최대 1마리
처음 아기상어 크기:2 (1초에 상하좌우 이동)
상어는 자기보다 큰 물고기 있는 칸 못지나감, 자신의 크기보다 작은 물고기만 먹을 수 있음
 => 상어랑 크기가 같으면 먹을 수는 없고 지나가는것만 가능
 
 1. 더이상 먹을 물고기 없는 경우=> 엄마 요청
 2. 먹을 수 있는 물고기가 1마리 => 먹으러 감
 3. 먹을 수 있는 물고리가 1마리 이상 => 가장 가까운 물고기 먹음
    => 거리가 가까운 물고기가 많은 경우 => 가장 위의 물고기 => 이때도 여러마이 이면 왼쪽 가장 위 물고기 먹음

물고기 먹으면 그 칸은 빈칸이 됨. 
상어의 크기와 동일한 물고기를 먹으면 1씩 증가 
엄마 요청하지 않고 물고기를 잡아먹을 수 있는지 작성
0: 빈칸
1~6: 각 칸의 물고기 크기
9: 상어 위치
'''


from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))
def findS(): # 처음 상어 위치 좌표 찾은 후 그 값을 0으로 변환
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 9:
                maps[i][j] = 0
                return (i,j)    

# 현재 상어 위치와 크기 정보를 입력으로 받음
def bfs(sPos, size):
    Q = deque()
    Q.append((*sPos,0))
    cur_size = size
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    visited = [[False]*N for _ in range(N)]
    visited[sPos[0]][sPos[1]] = True
    tmp = [] # 이동 가능한 후보들 담는 곳
    while Q:
        cur_y , cur_x , depth = Q.popleft()
        # 이동가능한 지점 확인
        for ddx , ddy in zip(dx , dy):
            nx, ny = cur_x + ddx , cur_y +ddy
            if 0<=nx<N and 0<= ny < N and maps[ny][nx] <= cur_size and not visited[ny][nx]:
                # 다음 위치가 0이거나 사이즈가 같은 경우는 큐에 삽입
                if maps[ny][nx] == 0 or maps[ny][nx] == size:
                    visited[ny][nx] = True
                    Q.append((ny,nx,depth+1))
                # 다음 위치가 0이 아닌 경우 즉 물고기 잡아 먹을 수 있는 경우 후보에 담기
                elif maps[ny][nx] < cur_size:
                    tmp.append((ny,nx,depth+1))
    # 최종 후보들 중에서 최단 거리이면서(depth 가 가장 작으면서) , y값이 가장 작고, x값이 작은 후보로 정렬 => 원하는 후보가 맨 뒤에 오도록 reverse 취함
    return sorted(tmp , key = lambda x : (x[2] , x[0] , x[1]), reverse=True)

        
        
            
S = findS()   
size = 2            
total_times = 0
numEatFish = 0
while 1:
    results = bfs(S , size)
    # 먹을 수 있는 물고기 위치가 반환된 경우 
    if len(results):
        y,x,depth = results.pop() # 리스트의 맨 마지막 정보 가져옴
        maps[y][x] = 0 #
        S = (y,x) # 다음 상어 위치 변경
        numEatFish +=1
        total_times += depth
        # 상어가 먹은 물고기 마리수에 따라 사이즈 변경
        if size == numEatFish:
            size +=1
            numEatFish =0
    else:
        # 먹을 수 있는 물고기가 없는 경우 
        print(total_times)
        break
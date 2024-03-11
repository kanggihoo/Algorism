'''
N N체스판, K개의 말, 말위에 말 올리기 가능
각 판은 흰,빨,파 중 하나
말위에 K개 말 놓고 시작 (1~K)번호, 이동 방향도 정해짐(상하좌우)
1번말 -> K번말 순서대로 이동, 올려진 말도 같이 이동, 
진행중 말이 4개 이상 쌓이면 게임 종료

- 이동하려는 칸이 흰색인 경우 그 칸으로 이동, 말이 있으면 가장 위에 올림
- 빨강 : 이동한 후 말 위에 올려진 말의 순서 반대로 , 해당 위치에 말이 있는 경우
        순서는 움직인말의 위에만 변경, 
- 파랑: 이동하려는 방향의 반대로 방향변경 후 이동, 이때 이동하려는 위치가 파랑인 경우
이동하지 않음
- 체스판 벗어나는 경우 => 파랑과 동일하게 동작
A->B->C =>> C B A 

0흰색,1빨,2파
1:오 , 2;왼 ,3:위 ,4:아래
'''
N, K = map(int , input().split())
maps = []
position = [[-1]*N for _ in range(N)]
for _ in range(N):
    maps.append(list(map(int , input().split())))
command = []
info =[[] for i in range(K)]
for _ in range(K):
    y,x,d =  map(int , input().split())
    command.append((y-1,x-1,d))
T = 0
def move(y,x,d):
    if d==1: #오
        ny , nx = ny , nx+1
        if nx == N:
            d = 2
            nx = x-1    
        return ny,nx,d
    elif d==2: # 왼
        ny , nx = ny , nx-1
        if nx <0:
            d = 1
            nx = x+1
        return ny,nx,d
    elif d==3: # 위
        ny , nx = ny-1 , nx
        if ny <0:
            d = 4
            ny = y+1
        return ny,nx,d
    elif d ==4:
        ny , nx = ny+1 , nx
        if ny ==N:
            d = 3
            ny = y-1
        return ny,nx,d
def action(y,x,idx , ny,nx,d,nd):
    color = maps[ny][nx]
    if color == 0: # 흰
        position[ny][nx] ,position[y][x] = idx , -1 # 위치 업데이트
        if position[ny][nx] != -1: # 자기 위쪽 정보 업데이트
            for tidx in info[position[ny][nx]]:
                info[tidx].extend(info[idx])
    elif color == 1:# 빨강
        position[ny][nx] ,position[y][x] = idx , -1 # 위치 업데이트
        tmp = info[idx].copy()
        tmp = tmp[::-1]
        if len(info[idx]) > 1: # 순서변경 
            for tidx , i in enumerate(tmp):
                info[i] = tmp[tidx+1:]
        if position[ny][nx] != -1: # 누군가 있는 경우
            for tidx in info[position[ny][nx]]:
                info[tidx].extend(tmp)
    elif color==2: # 파랑
        # 이전에도 파랑이었던 경우 방향만 변환?????
        if position[y][x] == 2:
    
    return ny,nx,nd
            
            
             
# 처음위치 초기화
for idx, c in enumerate(command):
    y,x,d = c
    info[y][x]=idx

while T <=1000:
    new_command = []
    for idx, c in enumerate(command):
        y,x , d = c
        ny,nx,nd = move(y,x,d)
        ny,nx,nd = action(y,x,idx,ny,nx,d,nd)
        # action
        # 각 info 길이 확인
        
        
        
        
        
        

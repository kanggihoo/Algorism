import sys
input = sys.stdin.readline


'''
파,토,파이어스톰,물복사 버그 , 새롭게 비바라기 가능
A[][] ; 저장된 물양 , (1,1)부터 , 
(N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름

구름 이동을 M번 명령 => 방향과 거리 , 방향은 8방향(정수로 1번부터 ) 

'''
N , M = map(int , input().split())
MAP = []
C = []
for _ in range(N):
    MAP.append(list(map(int , input().split())))
for _ in range(M):
    d,s = map(int , input().split())
    C.append((d,s))

clouds = [[N-1,0],[N-1,1] ,[N-2,0] , [N-2,1]]

def left(y,x,s):
    new_x = (x-(s %N) +N)%N
    return (y , new_x)
def right(y,x,s):
    new_x = (x+(s %N))%N
    return (y , new_x)
def up(y,x,s):
    new_y = (y-(s %N) +N)%N
    return (new_y , x)
def down(y,x,s):
    new_y = (y+(s %N))%N
    return (new_y , x)
    
def move(clouds,d,s):
    if d == 1:# 왼쪽이동
        for idx , (y,x) in enumerate(clouds):
            y , new_x = left(y,x,s)
            clouds[idx] = [y,new_x]
    elif d == 5: # 오른쪽이동
        for idx , (y,x) in enumerate(clouds):
            y , new_x = right(y,x,s)
            clouds[idx] = [y,new_x]
    elif d == 3: # UP
        for idx , (y,x) in enumerate(clouds):
            new_y , x = up(y,x,s)
            clouds[idx] = [new_y , x]
    elif d==7: # down
        for idx , (y,x) in enumerate(clouds):
            new_y , x = down(y,x,s)
            clouds[idx] = [new_y , x]
    elif d == 2: # 좌상단
        for idx , (y,x) in enumerate(clouds):
            y,new_x = left(y,x,s)
            new_y, x = up(y,x,s)
            clouds[idx] = [new_y,new_x]
    elif d== 4: # 우상단
        for idx , (y,x) in enumerate(clouds):
            y,new_x = right(y,x,s)
            new_y, x = up(y,x,s)
            clouds[idx] = [new_y,new_x]
    elif d== 6: # 우하단
        for idx , (y,x) in enumerate(clouds):
            y,new_x = right(y,x,s)
            new_y, x = down(y,x,s)
            clouds[idx] = [new_y,new_x]
    elif d== 8: # 좌하단
        for idx , (y,x) in enumerate(clouds):
            y,new_x = left(y,x,s)
            new_y, x = down(y,x,s)
            clouds[idx] = [new_y,new_x]
def wcopy(clouds):
    for y,x in clouds:
        cnt = 0
        for ny,nx in [(y-1,x-1) ,(y-1,x+1),(y+1,x-1),(y+1,x+1)]:
            if 0<=ny<N and 0<=nx<N and MAP[ny][nx] !=0:
                cnt +=1
        MAP[y][x] += cnt
def find_next(clouds):
    tmp = []
    pre = set([y*N+x for y,x in clouds])
    for i in range(N):
        for j in range(N):
            if MAP[i][j] >=2 and i*N+j not in pre:
                tmp.append((i,j))
                MAP[i][j] -=2
    return tmp
def show():
    for i in range(N):
        for j in range(N):
            print(MAP[i][j] , end = " ")
        print()
    print()
for d,s in C:
    move(clouds, d,s)
    # 각 칸의 물증가
    for y,x in clouds:
        MAP[y][x]+=1
    # 구름 사라짐
    # 물이 증가한 칸 물복사 
    wcopy(clouds)
    # 다음 구름 생성 , -2
    clouds = find_next(clouds)
    # print(clouds)
    # show()
tsum =0
for i in range(N):
    tsum+=sum(MAP[i])
print(tsum)
        
    


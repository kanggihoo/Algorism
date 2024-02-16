'''
공기청정기 설치
RxC 크기 , (r,c)칸에 있는 미세먼지 양 모니터링 (1부터시작)
공기청적기는 항상 1열 에 설치, 2행을 차지
각 칸의 미세먼지 양 : A_rc

1. 미세먼지 확산. (미세먼지 존재하는모든칸에서 동시에)
    - 인접 4방향으로(공기청정기 없거나, 칸이 없는 경우제외)
    - 확산되는 양은 A_rc / 5 소수점 버림
    - (r,c)에 남는 먼지는 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 
2. 공기청저기 동작
    - 위쪽 공기청정기 바람은 반시계방향 , 아래쪽은 시계방향
    - 바람방향 대로 미세먼지 한칸씩 이동
    - 공기청정기로 들어가는 미세먼지는 모두 정화

T초 지난 후 방에 남아 있는 미세먼지 양 구하기
'''
R , C , T = map(int , input().split())
room = []
for _ in range(R):
    room.append(list(map(int , input().split())))
# 공기청정기 설치된 곳 찾기 
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append((i,0))
        cleaner.append((i+1,0))
        break
def diffuse():
    tmp = [[0]*C for _ in range(R)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0] 
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                count = 0
                for ddy , ddx in zip(dy,dx):
                    ny , nx = i+ddy , j+ddx
                    if 0<=ny<R and 0<=nx<C and room[ny][nx] !=-1:
                        count +=1
                        tmp[ny][nx] += int(room[i][j]/5)
                # 현재 위치 업데이트
                tmp[i][j] -= (int(room[i][j]/5)*count)
    # tmp 값 반영
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp[i][j] 
                       
def ccw(upper):
    uy , ux = upper
    for i in reversed(range(uy-1)): # 
        room[i+1][0] = room[i][0]
    for i in range(1,C):
        room[0][i-1] = room[0][i]
    for i in range(1,uy+1):
        room[i-1][C-1] = room[i][C-1]
    for i in reversed(range(2,C)):
        room[uy][i] = room[uy][i-1]
    room[uy][1] = 0
def cw(lower):
    uy , ux = lower
    for i in range(uy+2,R):
        room[i-1][0] = room[i][0]
    for i in range(1,C):
        room[R-1][i-1] = room[R-1][i]
    for i in reversed(range(uy,R-1)):
        room[i+1][C-1] = room[i][C-1]
    for i in reversed(range(2,C)):
        room[uy][i] = room[uy][i-1]
    room[uy][1] =0

# def show():
#     for i in range(R):
#         for j in range(C):
#             print(f"{room[i][j]:4}" , end ="")
#         print()
#     print()
    
def operate_cleaner():
    upper = cleaner[0]
    lower = cleaner[-1]
    # 위쪽은 반시계 방향 , 아래는 시계방향 
    ccw(upper)
    cw(lower)
def sum(tmp):
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp[i][j]

for t in range(T):
    # 각 먼지 확산 
    # print("t : ", t)
    # show()
    diffuse()
    # 공기청정기 동작
    operate_cleaner()
    # show()
# 남은 먼지 계산
result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            result += room[i][j]
print(result) 
    

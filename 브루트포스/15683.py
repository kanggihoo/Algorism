'''
NxM 사무실
k개의 CCTV(5 종류)
사무실에는 벽이 있는데 CCTV는 벽을 통과 못함
CCTV는 90도 회전 가능 
0은 빈칸 , 6은 벽 , 1~5는 cctv 종류

이떄 CCTV 방향을 적절히 조절해서
사각지대의 초소크기 구하기.
(N,M) : 1~8
'''
N , M = map(int , input().split())
maps= []
for _ in range(N):
    maps.append(list(map(int , input().split())))
# CCtv 위치 찾고 
cctv = [[]*6] # (y,x,type)
for i in range(N):
    for j in range(M):
        if 1<=maps[i][j]<=5:
            type = maps[i][j]
            cctv[type].append((i,j))
# 방향 별 cctv 비추기
def cctv_area(y,x,d,map):
    if D==0:
        while x+1 < M or maps[y][x+1] !=6:
            x +=1
            if maps[y][x] == 0:
                map[y][x] = -1
    elif D==1:
        while y+1 < N or maps[y+1][x] !=6:
            y+=1
            if maps[y][x] == 0:
                map[y][x] = -1
    elif D==2:
        while x-1 >=0 or maps[y][x-1] !=6:
            x -=1
            if maps[y][x] == 0:
                map[y][x] = -1
    elif D==3:
        while y-1 >= 0 or maps[y-1][x] !=6:
            y-=1
            if maps[y][x] == 0:
                map[y][x] = -1


# cctv종류 별 방향 비추기


# 방향 별 반복
D = [0,1,2,3] # 0: 오 , 1: 아 , 2, 왼 , 3: 위


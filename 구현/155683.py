'''
사무실이 NxM 
총 K개의 CCTV (CCTV는 5종류 존재)
1. 한쪽 방향 감지 => 4방향 조절 가능
2. 양쪽 방향감지(방향 반대) => 2방향 조절
3. 양쪽 방향 감지(방향 수직) => 4방향
4. 3방향 감지  => 4방향
5. 4방향 감지
CCTV는 보는 방향의 전체 영역 탐지 가능(벽통과 못함)
CCTV 90도 회전만 가능, CCTV는 CCTV통과 가능
0: 빈칸 , 6:벽 1~5: CCTV 종류

CCTV 방향을 적절히 정해서 사각 지대의 최소 크기 계산
'''

N , M = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))
# cctv 위치찾기
cctv = []
for i in range(N):
    for j in range(M):
        if 1<=maps[i][j]<=5:
            cctv.append((i,j,maps[i][j])) # (y,x,type)
# 0 : 오 , 1: 아 , 2 : 왼 , 3 : 위
types = [
    [],
    [[0], [1] ,[2],[3]],
    [[0,2] , [1,3]],
    [[3,0] , [0,1] , [1,2] , [2,3]] ,
    [[2,3,0] , [3,0,1] , [0,1,2] , [1,2,3]],
    [[0,1,2,3]]
]
result = int(1e9)
# 0 : 오 , 1: 아 , 2 : 왼 , 3 : 위
def fill(y,x, directions , maps):
    for d in directions:
        sy  ,sx = y,x
        if d == 0:
            while sx+1 < M and maps[sy][sx+1] != 6:
                if maps[sy][sx+1] == 0:
                    maps[sy][sx+1] = 7
                sx+=1
        elif d==1:
            while sy+1 < N and maps[sy+1][sx] != 6:
                if maps[sy+1][sx] == 0:
                   maps[sy+1][sx] = 7
                sy+=1
        elif d==2:
            while sx-1 >=0 and maps[sy][sx-1] != 6:
                if maps[sy][sx-1] == 0:
                    maps[sy][sx-1] = 7
                sx-=1
        elif d==3:
            while sy-1 >=0 and maps[sy-1][sx] != 6:
                if maps[sy-1][sx] == 0:
                    maps[sy-1][sx] = 7
                sy-=1

    
def check(maps):
    cnt =0 
    for i in range(N):
        for j in range(M):
            if maps[i][j] ==0:
                cnt +=1
    return cnt
import copy
import sys 
# sys.setrecursionlimit(10**8)
def show(maps):
    for i in range(N):
        for j in range(M):
            print(f"{maps[i][j]:2}" , end = "")
        print()
    print()
def dfs(depth,maps):
    if depth == len(cctv):
        global result
        result = min(result , check(maps))
        return 
    y,x,cnum = cctv[depth]
    for directions in types[cnum]:
        tmp = copy.deepcopy(maps)
        fill(y,x, directions, tmp)
        # show(tmp)
        dfs(depth+1 , tmp)
        # show(maps)
        # tmp = copy.deepcopy(maps)
dfs(0,maps)
print(result)
        
            



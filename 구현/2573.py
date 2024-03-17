'''
바다 : 0
나머지 : 빙산높이 
바닷물에 접해있으면 빨리 줄어듬
동서남북으로 0의 개수에 따라 높이 줄어듬
한 덩어리 빙산 주어질때 두 덩어리 이상으로 분리되는 최소 시간 작성

'''
import sys
input = sys.stdin.readline
N , M = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))
    
Time = 0
def find_P():
    P = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                cnt = 0
                for y,x in [(i-1,j),(i+1,j) , (i,j-1) , (i,j+1)]:
                    if maps[y][x] ==0:
                        cnt +=1
                P.append((i,j,cnt))
    return P
from collections import deque
def check(S):
    Q = deque()
    sy,sx = S
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    Q.append((sy,sx))
    cnt =0
    visited = [[False]*M for _ in range(N)]
    visited[sy][sx] = True
    while Q:
        cy,cx = Q.popleft()
        cnt +=1
        for ddy , ddx in zip(dy,dx):
            ny, nx = cy+ddy , cx+ddx
            if maps[ny][nx] !=0 and not visited[ny][nx]:
                visited[ny][nx] = True
                Q.append((ny,nx))
    return cnt        

def show():
    for i in range(N):
        for j in range(M):
            print(f"{maps[i][j]:2}" , end="")      
        print()
    print()
    
while 1:
    P = find_P()
    if len(P):    
        start = None
        remain = 0
        for y,x,c in P:
            if maps[y][x] <= c:
                maps[y][x] =0
            else:
                if start is None:
                    start = (y,x)
                maps[y][x] -=c
                remain +=1
        # show()
        # 분리여부 확인
        Time+=1
        if start is None:
            print(0)
            break
        else:
            divied = check(start)
        # print(remain , divied)
        if divied ==0 :
            print(0)
            break
        elif remain != divied:
            print(Time)
            break
    else:
        print(Time)
        break
    
        
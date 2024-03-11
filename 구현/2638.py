'''
치즈 2
NxM 치즈 , 
각 치즈 격자의 4변 중 적어도 2변 이상이 공기와 해야 후 한 시간 후 녹음


'''
import sys
input = sys.stdin.readline
N , M = map(int , input().split())
maps= []
for _ in range(N):
    maps.append(list(map(int , input().split())))
    
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
T = 0
pre_chizz = 0
while 1: 
    visited = [[0]*M for _ in range(N)]
    Q = deque()
    Q.append((0,0)) # (y,x,step)
    visited[0][0] = 1
    chizz = 0
    while Q:
        cy,cx = Q.popleft()
        for ddy , ddx in zip(dy,dx):
            ny ,nx = cy+ddy , cx+ddx
            if 0<=ny < N and 0 <= nx < M :
                if visited[ny][nx] == 0 and maps[ny][nx] ==0:
                    visited[ny][nx] +=1
                    Q.append((ny,nx))
                elif maps[ny][nx] == 1:
                    visited[ny][nx] +=1
                    if visited[ny][nx] ==2:
                        chizz +=1
                        maps[ny][nx] = 0
    if chizz == 0:
        print(T)
        break
    T+=1
    
# def show():
#     for i in range(N):
#         for j in range(M):
#             print(f"{maps[i][j]:2}" , end="")
#         print()
# show()
    
    
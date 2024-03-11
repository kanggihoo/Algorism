'''
정사각형 판위에 치즈(회색)
판의 가장자리에는 치즈가 없으며, 치즈에는 하나 이상의 구멍이 존재

치즈는 공기와 접촉한 칸은 한시간 지나면 녹는다. 
치즈의 구멍 속에는 공기가 없지만 구멍을 둘어싼 치즈가 녹아 구멍이 열리면
구멍 속으로 공기가들어감,

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
    visited = [[False]*M for _ in range(N)]
    Q = deque()
    Q.append((0,0)) # (y,x,step)
    visited[0][0] = True
    chizz = 0
    while Q:
        cy,cx = Q.popleft()
        for ddy , ddx in zip(dy,dx):
            ny ,nx = cy+ddy , cx+ddx
            if 0<=ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                if maps[ny][nx] == 1:
                    chizz +=1
                    maps[ny][nx] =0
                elif maps[ny][nx] == 0:
                    Q.append((ny,nx))
    if chizz == 0:
        print(T)
        print(pre_chizz)
        break
    pre_chizz = chizz
    T+=1
    
# def show():
#     for i in range(N):
#         for j in range(M):
#             print(f"{maps[i][j]:2}" , end="")
#         print()
# show()
    
    
'''
MxN 미로 
빈방 또는 벽으로 이루어짐 
운영진은 여러명이지만 항상 같은 방에 존재 
상하좌우 이동
벽은 무기를 이용해 부수기 가능
(1,1)에 있는 운영진이 N,M 이동하기 위해 최소 몇개 부수어야 하는지
0 : 빈방
1: 벽


'''
# 0,1 너비 탐색
# from collections import deque

# N ,M = map(int , input().split())
# maps = []
# for _ in range(M):
#     maps.append(list(map(int , input())))

# visited= [[False]*N for _ in range(M)]
# Q = deque()
# Q.append((0,0,0))
# visited[0][0] = True
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# result = 1e6
# while Q:
#     cy,cx,cc = Q.popleft()
#     if cy == M-1 and cx == N-1:
#         result = min(result , cc)
#     for ddy , ddx in zip(dy,dx):
#         ny,nx = cy+ddy , cx+ddx 
#         if 0<=nx < N and 0<= ny < M and not visited[ny][nx]:
#             nc = maps[ny][nx] + cc
#             if maps[ny][nx] == 1:
#                 Q.append((ny,nx,nc))
#             else:
#                 Q.appendleft((ny,nx,nc))
#             visited[ny][nx] = True
            
# print(result)

# 다익 스트라 
import math
import heapq
from collections import deque

N ,M = map(int , input().split())
maps = []
for _ in range(M):
    maps.append(list(map(int , input())))
INF = math.inf
distance = [[INF]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
Q = []
heapq.heappush(Q,(0 , 0,0))
distance[0][0] = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = INF
while Q:
    cd , cy,cx = heapq.heappop(Q)
    for ddy , ddx in zip(dy,dx):
        ny,nx = cy+ddy , cx+ddx 
        if 0<=nx < N and 0<= ny < M and not visited[ny][nx]:
            nc = cd + maps[ny][nx]
            if distance[ny][nx] > nc:
                distance[ny][nx] = nc
                heapq.heappush(Q,(nc , ny,nx))
                visited[ny][nx] = True
print(distance[M-1][N-1])       
    
'''
n*n 바둑판 , 검 또는 흰 방
검은 방은 못들어감(0) , 흰방(1)은 움직이기 가능
0,0은 항상 흰방 , 우측 하단도 흰방
시작 => 끝방 
이때 검은 방 몇 개를 흰 방으로 바꾸어 최대한 적게 하고자 한다. 


'''
import sys
import heapq 
input = sys.stdin.readline
N = int(input())
hq = []
maps = []
for _ in range(N):
    maps.append(list(map(int , input().strip())))
# print(maps)
INF = float("inf")
distance = [[INF]*N for _ in range(N)]
distance[0][0] = 0
heapq.heappush(hq , (0,0,0))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
while hq:
    cost , y , x = heapq.heappop(hq)
    if distance[y][x] == INF:
        continue
    for ddy , ddx in zip(dy,dx):
        ny , nx = ddy+y , ddx+x
        if 0<=ny<N and 0<=nx<N :
            weight = 0
            if maps[ny][nx] == 0:
                 weight =1
            if distance[ny][nx] > cost+weight:
                distance[ny][nx] = cost+weight
                heapq.heappush(hq , (cost+weight , ny,nx))

print(distance[N-1][N-1])
# for i in range(N):
#     for j in range(N):
#         print(f"{distance[i][j]:3}" , end="")
#     print()    
    
    

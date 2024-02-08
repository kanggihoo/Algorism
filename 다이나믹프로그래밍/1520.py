'''
각 칸은 그 지점의 높이이며, 상하좌우 이동가능 
(0,0) 에서 출발하여 우측 하단으로 이동
이때 높이가 더 낮은 지점으로만 이동
이때 이동할 수 있는 모든 경로의 개수 구하시오.
세로 : M , 가로 N
'''
import sys
input = sys.stdin.readline
M , N = map(int , input().split())
maps = []
for _ in range(M):
    maps.append(list(map(int , input().split())))
# dfs 쓰면 재귀 호출 에러및 시간초가
# result = 0 
# dy = [1,-1,0,0]
# dx = [0,0,1,-1]
# def dfs(y,x , dy , dx):
#     if y == M-1 and x == N-1:
#         global result
#         result +=1
    
#     for ddx , ddy in zip(dx , dy):
#         ny , nx = y+ddy , x + ddx
#         if 0<= nx < N and 0<= ny < M and maps[y][x] > maps[ny][nx]:
#             dfs(ny , nx , dy,dx)
# dfs(0,0,dy ,dx)
# print(result)

# DP + DFS 조합
# https://hackids.tistory.com/109
D = [[-1]*N for _ in range(M)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs(y,x):
    if y == M-1 and x == N-1:
        return 1
    if D[y][x] !=-1: # 이미 가본 길
        return D[y][x]
        
    # 처음 가는 길
    ways = 0
    for ddy , ddx in zip(dy,dx):
        ny , nx = ddy+y , ddx+x
        if 0<= nx < N and 0<= ny < M and maps[y][x] > maps[ny][nx]:       
            ways +=bfs(ny,nx) # 현재 위치에서 목적지 까지 갈 수 있는 경우의 수가 몇개인지 계산
    
    D[y][x] = ways
    return ways
    
print(bfs(0,0))

# for i in range(M):
#     for j in range(N):
#         print(f"{D[i][j]:5}" , end="")
#     print()
        

            
    
    

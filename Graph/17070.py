'''
NxN의 집  (r,c) 각 위치는 1,1부터 시작
파이프는 2자리 차지, 회전 가능하며
파이프를 방향은 3가지 (오른쪽 , 아래 오른쪽 , 아래)

가로인 경우 2가지 이동가능
세로인 경우 2가지
대각선인 경우 3가지
0: 빈칸 , 1: 벽 (벽있으면 이동 x)

처음 위치는(1,1) , (1,2) 가로 방향으로 위치 
파이프의 끝을 (N,N) 이동 시키는 방법 구하기
'''
import sys
input = sys.stdin.readline
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))
# 방향은 R , D , RD 3가지 방향
direct = "R"

# def move(y,x,D): #(y,x)는 파이프 끝점
#     if D =="R": # 오른쪽 방향
#         dy ,dx,d =  [1,0] , [1,1] , ["RD" , "R"]
#         return dy, dx , d
#     elif D =="D": # 아래 방향
#         dy , dx , d = [1,1],[0,1],["D" , "RD"]
#         return dy, dx , d
#     else: # 아래 대각선 방향
#         dy , dx ,d= [0,1,1] , [1,1,0] , ["R","RD" , "D"]
#         return dy, dx , d

# from collections import deque
# def bfs():
#     Q = deque()
#     results = 0
#     Q.append((0,1,"R",1))   
#     while Q:
#         y,x,d,depth = Q.popleft()
#         if y==N-1 and x==N-1:
#             results+=depth
#         dy,dx,dd = move(y,x,d)
#         # 방향에서 따라서도 이동가능여부 다름
#         for idx ,(ddy,ddx) in enumerate(zip(dy,dx)):
#             ny,nx,nd = y+ddy , x+ddx , dd[idx]
#             if 0<=ny<N and 0<=nx<N and maps[ny][nx] ==0:
#                 if nd =="RD" and (maps[y+1][x] == 1 or maps[y][x+1] == 1):
#                     continue
#                 Q.append((ny,nx,nd,depth))
#     return results

# print(bfs())

# result = 0
# def dfs(y,x,d):
#     if y == N-1 and x ==N-1:
#         global result
#         result += 1
        
    
#     dy , dx ,dd = move(y,x,d)
#     for idx , (ddy , ddx) in enumerate(zip(dy,dx)):
#         ny , nx , nd = y+ddy , x + ddx , dd[idx]
#         if 0<=ny<N and 0<=nx<N and maps[ny][nx] ==0:
#                 if nd =="RD" and (maps[y+1][x] == 1 or maps[y][x+1] == 1):
#                     continue
#                 dfs(ny,nx,nd)
                
# dfs(0,1,direct)
# print(result)


# dp 풀이
# dp[r][c][d] d=0: 오른쪽 , d=1 : 아래 , d=2 : 대각선방향
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# dp 초기 위치 초기화
for i in range(1,N):
    if maps[0][i] ==1:
        break
    else:    
        dp[0][i][0] = 1

for i in range(1,N):
    for j in range(1,N):
        # 대각선 이동 가능여부
        if maps[i][j] == 0 and maps[i-1][j] ==0 and maps[i][j-1]==0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
        # 오른쪽 , 아래 이동 가능여부
        if maps[i][j] ==0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[N-1][N-1]))
    
    
            
            
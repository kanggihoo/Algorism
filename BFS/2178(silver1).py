import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
Miro = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
depth = [[0]*M for _ in range(N)]
for i in range(N):
    number = input()
    for j in range(M):
        Miro[i][j] = int(number[j])

# cur = (0,0)
# Q = deque()
# Q.append(cur)
# visited[0][0] = True
# depth[0][0] = 1
# # dx : 오른쪽, dy : 아래방향 (dx는 오르)
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# while Q:
#     cur = Q.popleft()
#     if cur == (N-1, M-1):
#         print(depth[cur[0]][cur[1]])
#         break
#     # 현재위치에서 이동해서 갈 수 있는 경우 Q에 삽입
#     for x,y in zip(dx , dy):
#         next_p = (cur[0]+y , cur[1]+x)
#         # next_p가 실제로 이동가능한 좌표인지 확인
#         if next_p[0] > N-1 or next_p[0] < 0 or next_p[1] > M-1 or next_p[1] < 0 :
#             continue
#         if Miro[next_p[0]][next_p[1]] != 0 and not visited[next_p[0]][next_p[1]]:
#             Q.append(next_p)
#             visited[next_p[0]][next_p[1]] = True
#             depth[next_p[0]][next_p[1]] = depth[cur[0]][cur[1]]+1




depth = [[1e9]*M for _ in range(N)]
cur = (0,0)        
visited[0][0] = True
depth[0][0] = 1
# dx : 오른쪽, dy : 아래방향 (dx는 오르)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y):
    
    c_x , c_y = x,y
    
    for ddx ,ddy in zip(dx , dy):
        n_x , n_y = ddx+c_x , ddy+c_y
        if n_x < 0 or n_x > M-1 or n_y < 0 or n_y > N-1 :
            continue
        if Miro[n_y][n_x] !=0 and not visited[n_y][n_x]:
            visited[n_y][n_x] = True
            depth[n_y][n_x] = min(depth[n_y][n_x] , depth[c_y][c_x]+1)
            dfs(n_x , n_y)
            visited[n_y][n_x] = False

dfs(0,0)
print(depth[N-1][M-1])
    



import sys
input = sys.stdin.readline
N , M = map(int , input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int , input().split())))
D = [[-1 for _ in range(M)] for _ in range(N)]
def dfs(x,y):
    if x==M-1  and y==N-1:
        return 1
    if D[y][x] !=-1:
        return D[y][x] 
    case = 0
    for nx , ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=nx < M and 0<=ny < N and MAP[y][x] > MAP[ny][nx]:
            case += dfs(nx,ny)
    D[y][x] = case
    return D[y][x]            

ans = dfs(0,0)
if ans == -1:
    print(0)
else:
    print(ans)

# for i in range(N):
#     for j in range(M):
#         print(D[i][j] , end = " ")
#     print()


    
    
        
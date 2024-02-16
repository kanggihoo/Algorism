N , M = map(int , input().split())
board = []
for _ in range(N):
    board.append(list(map(int , input().split())))
result = 0
visited = [[False]*M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def case1(y,x,iter,tsum):
    if iter ==4:
        global result
        result = max(result , tsum)
        return
    visited[y][x] = True
    for ddy ,ddx in zip(dy,dx):
        ny , nx = ddy+y , ddx+x
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            visited[ny][nx] = True
            case1(ny,nx,iter+1,tsum+board[y][x])
            visited[ny][nx] = False
    visited[y][x] = False
    return 
def case2(y,x,value):
    global result
     
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    for i in range(4):
        s = i
        tsum = value
        for j in range(3):
            ny , nx = y+dy[(i+j)%4] , x+dx[(i+j)%4]
            if ny < 0 or ny >=N or nx < 0 or nx >= M:
                break
            tsum += board[ny][nx]
        result = max(result , tsum)

for i in range(N):
    for j in range(M):
        
        case1(i,j,0,0)
        
        case2(i,j,board[i][j])

print(result)
            
        
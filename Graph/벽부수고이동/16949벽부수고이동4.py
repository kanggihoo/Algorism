import sys
input = sys.stdin.readline

'''
먼저 모든 0인지점에 대해 벽부지않고 이동가능한 개수 
BFS로 몇개있는지 찾고 백트래킹으로 해당 개수로 변경
벽이 숫자 1이어서 구분안되니 다른 걸로 변경

그리고 모든 벽에 대하여 자기 자신만 부수고 벽을 만나면 더이상
못가고, 벽이 아닌 앞에서 구한 값을 만나면 바로 멈추고 해당값을 누적해서
자기 자기 포함 모두 더함
이거는 BfS 보단 DFS가 편할듯?


'''
N , M = map(int , input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int , input().strip())))
ZERO_MAP = [[0]*M for _ in range(N)]
def find_zero_one():
    zero = []
    one = []
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                one.append((i,j))
            else:
                ZERO_MAP[i][j] = -1
                zero.append((i,j))
    return zero , one
from collections import deque
def bfs(y,x , visited):
    Q = deque()
    Q.append((y,x))
    result = [(y,x)]
    visited[y][x] = True
    tcnt = 0
    while Q:
        y , x = Q.popleft()
        tcnt +=1
        for ny, nx in [(y-1,x) , (y+1,x),(y,x-1),(y,x+1)]:
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and MAP[ny][nx] != 1:
                visited[ny][nx] = True
                Q.append((ny,nx))
                result.append((ny,nx))
    return result , tcnt

    
    
zeros , ones = find_zero_one()
visited = [[False]*M for _ in range(N)]
for idx ,zero in enumerate(zeros):
    if not visited[zero[0]][zero[1]]:
        result , tcnt = bfs(*zero , visited)
        for y,x in result:
            ZERO_MAP[y][x] = (idx,tcnt)
for y,x in ones :
    cnt = 1
    check = set()
    for ny,nx in [(y-1,x) , (y+1,x) , (y,x-1) , (y,x+1)]:
        if 0<=ny<N and 0<=nx<M and MAP[ny][nx] !=1 and ZERO_MAP[ny][nx][0] not in check:
            check.add(ZERO_MAP[ny][nx][0])
            cnt += ZERO_MAP[ny][nx][1]
    ZERO_MAP[y][x] = cnt % 10

    
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            print(0,end="") 
        else:
            print(ZERO_MAP[i][j] % 10, end = "")
    print()

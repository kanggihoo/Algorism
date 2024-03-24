import sys
input = sys.stdin.readline
from collections import deque
MAP = []
for _ in range(12):
    MAP.append(list(input().strip()))

def bfs(color , y, x , visited ,case):
    Q = deque()
    Q.append((y,x))
    visited[y][x] = True
    hist = [(y,x)]
    while Q:
        y,x = Q.popleft()
        
        for ny,nx in [(y-1,x) , (y+1,x) , (y,x-1) , (y,x+1)]:
            if 0<=ny<12 and 0<=nx <6 and not visited[ny][nx] and MAP[ny][nx] == color:
                Q.append((ny,nx))
                visited[ny][nx] = True
                hist.append((ny,nx))
    if len(hist) >=4:
        case.append(hist)
        
def break_block(case):
    for pos in case:
        for y, x in pos:
            MAP[y][x] = "."
def move_block(pre_start):
    for i in range(6):
        top = pre_start[i]
        if top >= 12:
            continue
        bottom = 11
        while bottom >=0 and MAP[bottom][i] !=".":
            bottom -=1
        if bottom ==-1:
            continue
        for idx in reversed(range(0, bottom+1)):
            if MAP[idx][i] != ".":
                MAP[bottom][i], MAP[idx][i] = MAP[idx][i] , "."
                bottom -=1
        pre_start[i] = bottom+1 
        
            
def show():
    for row in range(12):
        for col in range(6):
            print(MAP[row][col] , end="")
        print()
    print()
        
pre_start = [12]*6
for col in range(6):
    for row in range(12):
        if MAP[row][col] !=".":
            pre_start[col] = row
            break

ans = 0
while 1:
    visited = [[False]*6 for _ in range(12)]
    case = []
    for i in range(6):
        if pre_start[i] >= 12:
            continue
        idx=pre_start[i]
        while idx < 12:
            color = MAP[idx][i]
            if not visited[idx][i]:
                bfs(color , idx,i,visited , case)
            idx +=1
    # block 부수고 위치 내리기
    if len(case) >= 1: 
        ans +=1
         # 부수기
        break_block(case)
        # 하강
        move_block(pre_start)
        # 
        # print(pre_start)
        # show()
  
    else:
        break
print(ans)
    
   
    

        
    
    
    
                 
            
        
        
    


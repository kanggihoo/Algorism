'''
세로 N , 가로 M 
빨강, 파랑 구슬 1개씩
빨간 구슬이 먼저 빠져나와야함.
동시에 빨강 파랑이 나와도 실패

기울이는 동작을 그만하는 것을 더이상 구슬이 움직이지 않는 경우 
"." 빈칸
"#" 벽
"O" 구멍
"R" 빨 , "B" 파
최소 몇번만에 빨 수 있는지 출력
10번 이하로 못하는 -1출력
'''
import sys
input = sys.stdin.readline
N , M = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(input().strip()))
def find_position(maps):
    red , blue , hole= None , None , None
    for i in range(N):
        for j in range(M):
            if maps[i][j] == "R":
                red = (i,j)
            elif maps[i][j] =="B":
                blue = (i,j)
            elif maps[i][j] =="O":
                hole = (i,j)
    return red , blue , hole 

def move(y,x , d,visited):
    if d =="R":
        while maps[y][x+1] == ".":
            if maps[y][x+1] == "O":
                return y,x+1 , True
            x+=1
        return (y,x,False)
    elif d =="L":
        while maps[y][x-1] == ".":
            if maps[y][x-1] == "O":
                return y,x-1 , True
            x-=1
        return (y,x,False)
    elif d =="U":
        while maps[y-1][x] == ".":
            if maps[y-1][x] == "O":
                return y-1,x , True
            y-=1
        return (y,x,False)
    elif d=="D":
        while maps[y+1][x] == ".":
            if maps[y+1][x] == "O":
                return y+1,x , True
            y+=1
        return (y,x,False)

def is_enable_move(y,x): # 움직일 수 있으면 True ,  아니면 False 반환
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    if all(True if maps[ddy+y][ddx+x] =="#" else False for ddy , ddx in zip(dy,dx)):
        return False
    else:
        return True

def is_same_row(blue , red):
    if blue[0] == red[0]:
        s = min(blue[1] , red[1])
        e = max(blue[1] , red[1])
        row = blue[0]
        for i in range(s+1,e):
            if maps[row][i] == "#":
                return False
        return True
    else:
        return False 
def is_same_col(blue , red):
    if blue[1] == red[1]:
        s = min(blue[0] , red[0])
        e = max(blue[0] , red[0])
        col = blue[1]
        for i in range(s+1,e):
            if maps[i][col] == "#":
                return False
        return True
    else:
        return False

    
        
        
from collections import deque
red , blue , hole = find_position(maps)
result = -1
if is_enable_move(*red):
    print("사방 가로 막힘")
    print(result)
else:
    visited = [[False] * M for _ in range(N)]
    D = ["R" , "L" , "U" , "D"]
    Q = deque()
    Q.append((red , blue , 0)) 

    while Q:
        cred , cblue , step = Q.popleft()
        if step > 10:
            break
        # 4가지 방향에  따라 이동
        for d in D:
            nred , rflag = move(*cred , D , visited)
            nblue , bflag = move(*cblue , D , visited)

            
        
    


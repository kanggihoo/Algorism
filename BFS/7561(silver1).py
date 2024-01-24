'''
체스 나이트가 특정 칸으로 이동하기 위해 최소 몇번 움직이는가 => BFS


'''

def bfs():
    Q = deque()
    map = [[-1]*map_size for _ in range(map_size)]
    # 초기 위치 초기화
    map[cur_P[1]][cur_P[0]] = 0
    # 말이 움직일 수 있는 경우
    move_P = [(1,2) , (2,1) , (2,-1) , (1,-2) , (-1 , -2) , (-2 ,-1) , (-2 , 1) , (-1 , 2)]
    Q.append((cur_P))

    while Q:
        cur = Q.popleft()
        if cur[0] == tar_P[0] and cur[1] == tar_P[1]:
            print(map[cur[1]][cur[0]])
            break
        for dx ,dy in move_P:
            nx , ny = cur[0]+dx , cur[1]+dy
            if ((nx >=0 and nx < map_size) and (ny >=0 and ny < map_size)) and map[ny][nx] ==-1:
                Q.append((nx,ny))
                map[ny][nx] = map[cur[1]][cur[0]]+1
            
    
import sys
from collections import deque
T = int(input())
for _ in range(T):
    map_size = int(input())
    cur_P = list(map(int , input().split()))
    tar_P = list(map(int , input().split()))
    bfs()
   

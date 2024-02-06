'''
배추흰지렁이가 해충을 잡아 먹으면서 배추 보호
배추가 인접해 있으면 1마리의 지렁이만 필요
0: 배추 없는 땅
1: 배추 심어진 땅
'''

import sys
from collections import deque
def BFS(x:int , y:int):
        Q = deque()
        Q.append((x,y))
        arr[y][x] = 0
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        while Q:
            cur = Q.popleft()
            for ddx , ddy in zip(dx , dy):
                next_x , next_y = cur[0]+ddx , cur[1]+ddy
                if next_x >= 0 and next_x <=M-1 and next_y >= 0 and next_y <= N-1 and arr[next_y][next_x] ==1:
                    Q.append((next_x,next_y))
                    arr[next_y][next_x] = 0
                    
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M , N , K = map(int , input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x ,y = map(int , input().split())
        arr[y][x] = 1

    # find all position
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                BFS(j,i)
                cnt +=1
    print(cnt)
            
